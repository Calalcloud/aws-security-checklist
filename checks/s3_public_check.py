import boto3
from botocore.exceptions import ClientError

def check_s3_public():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets().get('Buckets', [])
    public_found = []

    for b in buckets:
        name = b['Name']
        # First check bucket ACL
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            for grant in acl['Grants']:
                grantee = grant.get('Grantee', {})
                if grantee.get('Type') == 'Group' and 'AllUsers' in grantee.get('URI', ''):
                    public_found.append(name)
                    break
        except ClientError:
            continue

        # Next check bucket policy
        try:
            policy = s3.get_bucket_policy(Bucket=name)['Policy']
            if '"Principal":"*"' in policy:
                public_found.append(name)
        except ClientError:
            pass

    if public_found:
        print("[!] Public S3 buckets found:")
        for b in set(public_found):
            print(f"  - {b}")
    else:
        print("[✓] No public S3 buckets detected")

if __name__ == "__main__":
    print("Running S3 public bucket audit...\n")
    check_s3_public()

