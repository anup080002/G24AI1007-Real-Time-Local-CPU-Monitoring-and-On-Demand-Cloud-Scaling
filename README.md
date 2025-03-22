# 📈 Assignment 3 – CPU Monitoring & Auto-Scaling to AWS EC2

This project monitors CPU usage on a local Ubuntu VM using Prometheus and Node Exporter. When CPU exceeds 75%, a Python script triggers an AWS EC2 instance launch using AWS CLI. A Flask app is deployed on the new instance for verification.

## 🧱 Project Structure
- `monitor.py`: CPU monitoring script
- `scale_up.sh`: AWS CLI EC2 launch script
- `app.py`: Flask web app (deployed on EC2)
- `prometheus.yml`: Prometheus config
- `.gitignore`: Files to exclude from GitHub
- `README.md`: This file

## 🚀 How It Works
1. Prometheus scrapes system metrics from Node Exporter.
2. `monitor.py` checks CPU usage every 5s.
3. If CPU > 75%, it calls `scale_up.sh`.
4. `scale_up.sh` uses AWS CLI to launch a new EC2 instance.
5. Flask app runs on EC2 (port 80), accessed via public IP.

## 🔧 Prerequisites
- Ubuntu 22.04 VM (Hyper-V)
- AWS IAM credentials (configured via `aws configure`)
- Key pair and security group on AWS
- Prometheus and Node Exporter installed locally

## 📈 Prometheus Query
To visualize CPU usage:


## 🧪 Testing
- Simulate load with `stress --cpu 4 --timeout 30s`
- Check EC2 dashboard for new instances
- Access Flask at `http://<EC2-IP>`

## 📸 Screenshots
_Add screenshots here as needed._

## 👤 Author
Your Name – Anupkumar Pandey
