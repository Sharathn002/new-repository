pipeline {
  agent any
  stages {
    stage('version of python') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('version of pip') {
      steps {
        sh 'pip --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 Silencing.py'
      }
    }
  }
}
