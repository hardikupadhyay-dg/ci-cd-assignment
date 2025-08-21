pipeline {
  agent any

  environment {
    PIP_DISABLE_PIP_VERSION_CHECK = '1'
    PIP_NO_CACHE_DIR = '1'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Test (in Docker)') {
      steps {
        script {
          docker.image('python:3.12-slim').inside {
            sh '''
              python -m pip install --upgrade pip
              pip install pytest build
              pytest -q --junitxml=reports/junit.xml
            '''
          }
        }
      }
      post {
        always {
          junit 'reports/junit.xml'
        }
      }
    }

    stage('Package (wheel)') {
      steps {
        script {
          docker.image('python:3.12-slim').inside {
            sh '''
              python -m pip install --upgrade pip
              pip install build
              python -m build
            '''
          }
        }
      }
      post {
        success {
          archiveArtifacts artifacts: 'dist/*', fingerprint: true
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          // Image name can be anything locally; change if you plan to push to a registry
          def img = docker.build("calcapp:${env.BUILD_NUMBER}")
          echo "Built image: ${img.id}"
        }
      }
    }
  }
}
