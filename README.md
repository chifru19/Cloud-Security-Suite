🛡️ Cloud Security & DevSecOps Suite
An automated security auditing and remediation system for AWS S3 (simulated via LocalStack). This project demonstrates a full DevSecOps loop: Detect → Log → Visualize → Remediate.

🚀 Features
Automated Auditing: Python-based scanner checks for public S3 buckets.

Real-time Dashboard: Streamlit UI for monitoring security drift and compliance.

One-Click Remediation: Instant "Secure All" button to fix exposed infrastructure.

Infrastructure as Code: Managed via Terraform and Docker Compose.

🏗️ Quick Start
Start the Environment:

Bash
docker-compose up -d
Trigger a Manual Scan:

Bash
docker-compose run security-auditor python analyze.py
View the Dashboard:
Navigate to http://localhost:8501

🛠️ Tech Stack
Cloud: LocalStack (AWS Simulation)

Database: PostgreSQL

App: Streamlit (Python)

Security: Boto3, TruffleHog (Secret Scanning)

🛡️ Network-Guard-Forensics
🚀 Security Hardening & CI/CD
This project utilizes automated security auditing via Checkov to ensure a hardened, production-ready environment.

Key Implementation Details:
Vulnerability Remediation: Successfully resolved CKV_DOCKER_3 by transitioning from root execution to a dedicated, non-privileged appuser. This follows the Principle of Least Privilege, significantly reducing the attack surface.

System Resilience: Implemented native Docker HEALTHCHECK instructions (CKV_DOCKER_2) to allow container orchestrators to automatically monitor and recover the analysis process.

Infrastructure as Code (IaC) Auditing: Integrated security scanning into the GitHub Actions pipeline to catch misconfigurations in Terraform and Docker assets before deployment.

📩 Contact & Portfolio
Website: frankfru.com

GitHub: chifru19

LinkedIn: [https://www.linkedin.com/feed/]
