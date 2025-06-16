

import boto3

def check_mfa_enabled():
    iam = boto3.client('iam')
    insecure = []
    for u in iam.list_users()['Users']:
        devs = iam.list_mfa_devices(UserName=u['UserName'])['MFADevices']
        if not devs:
            insecure.append(u['UserName'])
    if insecure:
        print("[!] No MFA:", insecure)
    else:
        print("[✓] All users have MFA")

if __name__ == "__main__":
    print("🔍 Running MFA check...\n")
    check_mfa_enabled()

