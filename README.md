# 🛡️ Cloud-Security-Suite: Forensics, DevSecOps & CDR

A professional-grade security repository demonstrating a complete pivot from **Network Forensics** to **Cloud Security Engineering**. This suite features real-time threat detection, automated self-healing cloud remediation, and hardened CI/CD pipelines.

---

## 🏗️ Project 1: Cloud-Native DevSecOps Pipeline
**Focus:** Infrastructure-as-Code (IaC) Hardening & Supply Chain Security

* **Security Guardrails:** Integrated **Checkov** into GitHub Actions to scan Terraform and Docker configurations for 19+ common vulnerabilities.
* **Container Hardening:** Engineered a Dockerfile using non-root user execution and minimal base images to reduce the attack surface.
* **Proof of Work:**
![Pipeline Success](./pipeline_success.jpg.png)

---

## ☁️ Project 2: Real-Time Cloud Audit & Auto-Remediation
**Focus:** Active Compliance & Automated Self-Healing

* **Self-Healing Infrastructure:** Developed `security_audit.py` using **Boto3** to identify and automatically remediate non-compliant S3 buckets.
* **Zero-Cost Simulation:** Leveraged **LocalStack** to build and test cloud security tools in an isolated, mock AWS environment.
* **Live Status:**
✅ `Starting Real-Time Audit... No buckets found. Environment is clean.`

---

## 🚨 Project 3: Cloud Detection & Response (CDR)
**Focus:** Intrusion Detection & Behavioral Analysis

* **Custom IDS Engine:** Developed `cloud_detection.py` to monitor real-time API traffic and identify "Brute Force" patterns.
* **Rate-Limiting Alerts:** Triggers a **CRITICAL** alert if more than 5 requests are detected in under 3 seconds.
* **Live Detection Output:**
```text
🚨 CRITICAL ALERT: Rapid API activity detected! Possible Brute Force Attack.
