pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/VivekJha2k05/Portfolio-Docker-Compose',branch: 'main' 
      }
    }
    stage('Build') {
      steps {
        sh 'docker-compose build'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}

