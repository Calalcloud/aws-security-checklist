import boto3

def check_security_groups_open():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()
    insecure = []

    for sg in response['SecurityGroups']:
        for perm in sg.get('IpPermissions', []):
            # Check IPv4 CIDRs
            for ip_range in perm.get('IpRanges', []):
                if ip_range.get('CidrIp') == '0.0.0.0/0':
                    insecure.append((sg['GroupId'], sg['GroupName'], perm.get('FromPort'), perm.get('ToPort')))
            # Check IPv6 CIDRs
            for ipv6 in perm.get('Ipv6Ranges', []):
                if ipv6.get('CidrIpv6') == '::/0':
                    insecure.append((sg['GroupId'], sg['GroupName'], perm.get('FromPort'), perm.get('ToPort')))

    if insecure:
        print("[!] Secure groups allowing public ingress:")
        for sgid, name, frm, to in insecure:
            port_desc = f"{frm}-{to}" if frm is not None and to is not None else "all ports"
            print(f"  - {name} ({sgid}): opens {port_desc} to the world")
    else:
        print("[✓] No security groups with public ingress found")

if __name__ == "__main__":
    print("🔍 Running security groups public access check...\n")
    check_security_groups_open()

