import boto3

def check_cloudtrail_logging():
    ct = boto3.client('cloudtrail')
    trails = ct.describe_trails(includeShadowTrails=True)['trailList']
    if not trails:
        print("[!] No CloudTrail trails found!")
        return

    issues = []
    for t in trails:
        name = t.get('Name')
        is_multi = t.get('IsMultiRegionTrail')
        sink_bucket = t.get('S3BucketName')
        status = ct.get_trail_status(Name=name)
        is_logging = status.get('IsLogging', False)

        if not is_logging:
            issues.append(f"{name}: not logging")
        if not is_multi:
            issues.append(f"{name}: not multi-region")
        if not sink_bucket:
            issues.append(f"{name}: no S3 bucket configured")

    if issues:
        print("[!] CloudTrail issues detected:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("[✓] CloudTrail properly configured and logging")

if __name__ == "__main__":
    print("🔍 Running CloudTrail configuration check...\n")
    check_cloudtrail_logging()
