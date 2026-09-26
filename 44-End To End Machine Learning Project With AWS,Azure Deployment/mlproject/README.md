# End to End Machine Learning Project

## 1. Docker Build Checked

## 2. GitHub Workflow

## 3. IAM User in AWS

---

# Docker Setup in EC2 Commands to be Executed

### Optional

```bash
sudo apt-get update -y

sudo apt-get upgrade
```

### Required

```bash
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

---

# Configure EC2 as Self-Hosted Runner

Configure the EC2 instance as a **GitHub Actions self-hosted runner**.

---

# Setup GitHub Secrets

Add the following secrets to your GitHub repository:

```text
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION=us-east-1

AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME=simple-app
```
