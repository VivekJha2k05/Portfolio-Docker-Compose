pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/VivekJha2k05/docker-compose-webapp.git'
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

