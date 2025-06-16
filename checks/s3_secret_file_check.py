import boto3

# List of suspicious filenames that might contain secrets
SENSITIVE_FILENAMES = [
    ".env", "config.json", "secrets.json", "credentials.txt", 
    "aws_credentials.txt", ".aws/credentials", "settings.py"
]

def check_s3_secret_files():
    s3 = boto3.client("s3")
    findings = []

    try:
        buckets = s3.list_buckets()["Buckets"]
        for bucket in buckets:
            bucket_name = bucket["Name"]
            print(f"Scanning bucket: {bucket_name}")

            try:
                objects = s3.list_objects_v2(Bucket=bucket_name)
                if "Contents" in objects:
                    for obj in objects["Contents"]:
                        key = obj["Key"]
                        for name in SENSITIVE_FILENAMES:
                            if name in key:
                                findings.append((bucket_name, key))
            except Exception as e:
                print(f"  [-] Could not access {bucket_name}: {e}")

    except Exception as e:
        print(f"Error listing buckets: {e}")

    return findings

