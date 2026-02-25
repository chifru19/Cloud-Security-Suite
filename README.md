# Network Guard: Forensic & Security Audit Tool

A Python-based network analysis tool that processes PCAP files to visualize traffic patterns, calculate network latency, and audit for unencrypted credential leaks.

## 📊 Project Statistics
* **Total Packets Analyzed:** 15,467
* **Average Latency:** 32.95 ms
* **Security Alerts:** 3 potential cleartext leaks identified.

## 🛠️ Features
* **Automated Forensic Analysis:** Uses the Scapy library to parse raw packet data.
* **Credential Sniffer:** Scans unencrypted payloads for keywords like `pwd`, `auth`, and `user`.
* **Traffic Visualization:** Generates distribution reports for IP sources and protocols.

## 📈 Visual Reports
### Top Traffic Sources
![Top Talkers](top_talkers.png)

### Protocol Breakdown
![Protocol Distribution](protocol_distribution.png)

## 🚀 Technical Achievements
* Automated the ingestion of large-scale capture files.
* Implemented signature-based detection for PII (Personally Identifiable Information).
* Optimized data processing for 15k+ packets into actionable visual insights.
## 🚀 How to Run the Security Audit
This tool is designed to be run as a secure, isolated container.

1. **Build the hardened image:**
   `docker build -t cloud-audit-tool .`

2. **Run the automated scan:**
   `docker run --rm cloud-audit-tool`
# Pull the image file you just uploaded to your local machine
git pull origin main

# Add the image link to your README.md
echo -e "\n### 📈 Pipeline Proof of Work\n![DevSecOps Success](./pipeline_success.jpg.png)"
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
**Focus:** Active Compliance & FinOps-Safe Automation

* **Self-Healing Infrastructure:** Developed `security_audit.py` using **Boto3** to identify and automatically delete non-compliant S3 buckets in real-time.
* **Zero-Cost Simulation:** Leveraged **LocalStack** to build and test cloud security tools in a fully isolated, mock AWS environment.
* **Technical Achievement:** Automated the "Mean Time to Repair" (MTTR) by programmatically remediating misconfigurations without human intervention.

---

## 🚨 Project 3: Cloud Detection & Response (CDR)
**Focus:** Intrusion Detection & Behavioral Analysis

* **Custom IDS Engine:** Developed `cloud_detection.py` to monitor real-time API traffic and identify "Brute Force" or "Port Scanning" patterns.
* **Rate-Limiting Alerts:** Implemented threshold-based logic that triggers a **CRITICAL** alert if more than 5 requests are detected in under 3 seconds.
* **Live Detection Output:**
```text
🚨 CRITICAL ALERT: Rapid API activity detected! Possible Brute Force Attack.

