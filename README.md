# 🚀 Portfolio Web App with Docker Compose

A personal portfolio website built using **Flask**, containerized with **Docker**, and orchestrated using **Docker Compose**.  
This project demonstrates my skills in DevOps, containerization, and cloud deployment.

---

## 📌 Features

- Professional portfolio website with About, Skills, Projects, and Contact sections
- Flask backend serving a responsive HTML/CSS frontend
- Multi‑container setup with Flask (web) + MySQL (db)
- Dockerized for portability and easy deployment
- Ready for CI/CD integration with Jenkins
- Deployable on AWS EC2

---

## 🛠 Tech Stack

- **Frontend/Backend**: Flask, HTML, CSS
- **Database**: MySQL
- **Containerization**: Docker, Docker Compose
- **CI/CD**: Jenkins (pipeline ready)
- **Cloud**: AWS EC2

---

## 📂 Project Structure

Portfolio-Docker-Compose/
│── docker-compose.yml        # Defines services (web + db)
│── Jenkinsfile               # CI/CD pipeline definition
│── app/
│   ├── app.py                # Flask application
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile            # Web service Dockerfile
│── README.md                 # Project documentation

---

## ⚙️ Setup Instructions

### 0. Prerequisites
Make sure you have the following installed:

#### Install Docker

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
docker --version

#### Install Docker Compose

# Create the CLI plugins directory
sudo mkdir -p /usr/libexec/docker/cli-plugins/

# Download the binary (adjust architecture if necessary, e.g., x86_64 or aarch64)
sudo curl -SL "https://github.com/docker/compose/releases/latest/download/docker-compose-linux-$(uname -m)" -o /usr/libexec/docker/cli-plugins/docker-compose

# Make it executable
sudo chmod +x /usr/libexec/docker/cli-plugins/docker-compose

# Verify installation
docker compose version

1. Clone the repository

git clone https://github.com/VivekJha2k05/Portfolio-Docker-Compose.git
cd Portfolio-Docker-Compose

2. Build and run with Docker Compose

docker compose up -d --build

3. Access the app

Homepage → http://localhost:5000
DB Check → http://localhost:5000/check

🌐 Deployment on AWS EC2

1. Launch an Ubuntu EC2 instance

2. Install Docker + Docker Compose (see prerequisites above)

3. Clone this repo and run:

  git clone https://github.com/VivekJha2k05/Portfolio-Docker-Compose.git
  cd Portfolio-Docker-Compose
  docker compose up -d --build

4.Configure inbound rules in your EC2 Security Group:

Port range = 5000

Source = 0.0.0.0/0

5. Access via:

   http://<EC2-Public-IP>:5000
   http://<EC2-Public-IP>:5000/check

🛠 Troubleshooting

. Permission denied when running Docker  

→ Add your user to the Docker group:

  sudo usermod -aG docker $USER
  newgrp docker

. Port already in use  

→ Stop the conflicting service or change the port in docker-compose.yml.

. Container build errors  

→ Ensure your Dockerfile starts with:

  FROM python:3.9-slim
  and is named exactly Dockerfile.

