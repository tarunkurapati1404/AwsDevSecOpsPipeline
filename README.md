# 🚀 End-to-End DevSecOps Pipeline & AWS Deployment

A production-ready, automated DevSecOps project demonstrating CI/CD, Infrastructure as Code (IaC), Configuration Management, and Security Scanning.

## 🏗️ Project Architecture
```text
[Developer] 
    │ (git push)
    ▼
[GitHub Actions CI] ──▶ [SAST: Bandit] ──▶ [SCA: Snyk Dependency Scan]
    │ (Success)
    ▼
[Terraform] ──▶ Provisions AWS EC2 (Ubuntu) + Security Group + SSH Keys
    │ 
    ▼
[Ansible] ──▶ Configures Server: Installs Python, Deploys Flask App, Sets up Node Exporter
    │
    ▼
[AWS EC2 Instance] ──▶ Live Flask App (Port 5000) + Metrics Endpoint (Port 9100)
```

## 🛠️ Tech Stack
- **Version Control**: Git & GitHub
- **CI/CD**: GitHub Actions
- **Security (DevSecOps)**: Bandit (SAST), Snyk (Software Composition Analysis)
- **Infrastructure as Code (IaC)**: Terraform (AWS Provider)
- **Configuration Management**: Ansible
- **Cloud**: AWS (EC2, Security Groups)
- **Monitoring**: Prometheus Node Exporter
- **Application**: Python, Flask

## ✨ Key Features & Security Highlights
1. **Dynamic AMI Fetching**: Uses Terraform `data` sources to always fetch the latest Ubuntu 22.04 AMI.
2. **Secure Key Management**: SSH keys are generated locally, permissions locked (`chmod 400`), and strictly excluded from Git via `.gitignore`.
3. **Idempotent Deployment**: Ansible ensures the server configuration is repeatable and consistent.
4. **Shift-Left Security**: Automated SAST and dependency scanning on every `push` and `pull_request`.

## 🚀 How to Deploy
1. **Clone & Navigate**: `git clone <repo-url> && cd aws-devsecops-demo`
2. **Configure AWS**: Set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.
3. **Provision Infrastructure**: 
   ```bash
   cd terraform
   terraform init
   terraform apply -auto-approve
   ```
4. **Deploy Application**: 
   ```bash
   ansible-playbook -i inventory.ini ../deploy.yml
   ```
5. **Verify**: `curl http://<EC2_PUBLIC_IP>:5000/health`

## 🛡️ Security Best Practices Applied
- `.gitignore` strictly blocks `.pem`, `.tfstate`, and `.tfstate.backup` files.
- Security Groups restrict traffic to only SSH (22), App (5000), and Metrics (9100).
- Bandit security warnings are reviewed and documented (e.g., `# nosec` for intentional network binding).
