
# AWS Security Checklist

A collection of Python scripts to automate security audits on AWS environments.  
This project helps identify common misconfigurations such as missing MFA, public S3 buckets, open security groups, and exposed secrets.

---

## ✨ Features

- ✅ Check if AWS users have MFA enabled  
- ✅ Detect public S3 buckets  
- ✅ Identify security groups with public ingress rules  
- ✅ Verify if CloudTrail logging is enabled  
- ✅ Scan S3 buckets for potentially exposed secret files  

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Calalcloud/aws-security-checklist.git
cd aws-security-checklist
````

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# or
.venv\Scripts\activate     # For Windows
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧪 Run the Checks

### Run all checks:

```bash
python main.py
```

### Run individual checks (example):

```bash
python checks/s3_public_check.py
```

---

## 📁 Project Structure

```bash
aws-security-checklist/
├── checks/                   # Contains all individual audit scripts
│   ├── mfa_check.py
│   ├── s3_public_check.py
│   ├── security_groups_check.py
│   ├── cloudtrail_check.py
│   └── s3_secret_file_check.py
├── fixes/                    # (Optional) Scripts to auto-fix misconfigurations
├── main.py                   # Entry point to run all checks
├── requirements.txt
└── README.md
```

---

## ✅ Contributing

Feel free to fork this project and add more security checks or improvements.
Pull requests are welcome!

---

## 📘 License

This project is open-source and available under the [MIT License](LICENSE).

