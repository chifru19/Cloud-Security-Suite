# 🛡️ Cloud Security & DevSecOps Suite

Bridging the gap between detection and defense with an automated DevSecOps loop. 

An automated security auditing and remediation system for AWS S3 (simulated via LocalStack). This project demonstrates a full DevSecOps loop: **Detect → Log → Visualize → Remediate.**

---

## 🔗 Profile & Contact

* **Website:** [frankfru.com](https://frankfru.com)
* **GitHub:** [chifru19](https://github.com/chifru19)
* **LinkedIn:** [Connect on LinkedIn](https://www.linkedin.com/in/frank-fru/)

---

## 🚀 Features

* **Automated Auditing:** Python-based scanner checks for public S3 buckets.
* **Real-time Dashboard:** Streamlit UI for monitoring security drift and compliance metrics.
* **One-Click Remediation:** Instant "Secure All" button to programmatically fix exposed cloud infrastructure.
* **Infrastructure as Code (IaC):** Complete infrastructure management via Terraform and Docker Compose.
* **Continuous Integration:** Automated security scanning workflow checks infrastructure templates and container environments on every code push.

---

## 🛠️ Tech Stack

* **Cloud Simulation:** LocalStack (AWS Simulation)
* **Database:** PostgreSQL
* **Frontend/App:** Streamlit (Python)
* **Security & Auditing:** Boto3, Checkov (IaC Analysis), TruffleHog (Secret Scanning)
* **Orchestration:** Docker, Docker Compose, GitHub Actions

---

## 🛡️ Network-Guard-Forensics: Security Hardening & CI/CD

This project utilizes automated security auditing via Checkov to ensure a hardened, production-ready environment.

### Key Implementation Details
* **Vulnerability Remediation:** Successfully resolved `CKV_DOCKER_3` by transitioning from root execution to a dedicated, non-privileged `appuser`. This follows the Principle of Least Privilege, significantly reducing the attack surface.
* **System Resilience:** Implemented native Docker `HEALTHCHECK` instructions (`CKV_DOCKER_2`) to allow container orchestrators to automatically monitor and recover the analysis process.
* **Infrastructure as Code (IaC) Auditing:** Integrated security scanning into the GitHub Actions pipeline to catch misconfigurations in Terraform and Docker assets before deployment.

---

## 🔧 Engineering Iterations & Troubleshooting Journey

Reaching a fully automated green pipeline required extensive debugging, pipeline optimization, and deep dives into container security compliance. Below is a breakdown of how the architecture was hardened through active troubleshooting:

### 1. Infrastructure Hardening & S3 State Locks (Commits #1 - #5)
* **The Challenge:** Initial environments suffered from data preservation issues, configuration drift, and intermittent Terraform state locks during parallel pipeline runs.
* **The Fix:** Configured robust bucket compliance profiles by enforcing multi-layer encryption and explicit `public_access_block` modules. Resolved deployment blockages by optimizing remote state backends, adding automated remediation scripts, and appending lifecycle configurations to manage access logs cleanly.

### 2. Container Hardening & Checkov Compliance (Commits #6 - #10)
* **The Challenge:** Early Docker builds relied on standard, bulky environments executing as the root user. Automated scanning flagged critical vulnerabilities regarding access levels and container health visibility.
* **The Fix:** Hardened the Docker configurations through iterative iterations:
  * **Vulnerability Remediation (CKV_DOCKER_3):** Transitioned away from root execution to a dedicated, non-privileged `appuser`, adhering strictly to the Principle of Least Privilege.
  * **System Resilience (CKV_DOCKER_2):** Implemented native Docker `HEALTHCHECK` instructions, allowing container orchestrators to automatically monitor and safely recover the analysis processes.
  * **Base Image Optimization:** Migrated the environment fully to a `python:3.9-slim-buster` base image (#22). This stripped out unneeded binaries, reducing the attack surface area and fixing security failures.

### 3. CI/CD Workflow Stability & Scanning Fixes (Commits #11 - #16)
* **The Challenge:** The GitHub Actions workflow (`cloud-security.yml`) initially encountered runner failures, environment mismatches, and execution errors during automated code evaluation.
* **The Fix:** Analyzed logs line-by-line to adjust the CI pipeline sequencing. Refactored the workflow file to isolate linting, stabilize dependencies, and logically order security analysis tools so that misconfigurations in Terraform or Docker layers are blocked *before* deployment actions can trigger.

---

## 🏗️ Quick Start

### 1. Start the Environment
```bash
docker-compose up -d
2. Trigger a Manual Scan
Bash
docker-compose run security-auditor python analyze.py
3. View the Dashboard
Navigate to http://localhost:8501 inside your web browser.

📩 Contact & Portfolio
Website: frankfru.com

GitHub: chifru19

LinkedIn: https://www.linkedin.com/in/frank-fru/

📄 License
This project is licensed under the MIT License.
