from checks import mfa_check, s3_public_check, security_groups_check, cloudtrail_check, s3_secret_file_check

if __name__ == "__main__":
    print("Starting security audit...\n")
    mfa_check.check_mfa_enabled()
    s3_public_check.check_s3_public()
    security_groups_check.check_security_groups_open()   
    cloudtrail_check.check_cloudtrail_logging()

    print("\n[🔎] Checking for secret files in S3 buckets...")
    secret_files = s3_secret_file_check.check_s3_secret_files()
    if secret_files:
        print("[!] Possible secret files found:")
        for bucket, key in secret_files:
            print(f"    - Bucket: {bucket} | File: {key}")
    else:
        print("[✓] No exposed secret files found in S3 buckets.")
