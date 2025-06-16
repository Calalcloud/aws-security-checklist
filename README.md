# AWS Security Checklist

A collection of Python scripts to automate security audits on AWS environments.  
This project helps identify common misconfigurations like missing MFA, public S3 buckets, open security groups, and exposed secrets.

## Features

- Check if AWS users have MFA enabled
- Detect public S3 buckets
- Find security groups with public ingress rules
- Verify CloudTrail logging is enabled
- Scan S3 buckets for potentially exposed secret files

## Installation

1. Clone the repo:  
```bash
git clone https://github.com/Calalcloud/aws-security-checklist.git
cd aws-security-checklist


```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows-

pip install -r requirements.txt


Run all checks:

```bash

python main.py

Run individual checks


```bash

python checks/s3_public_check.py






