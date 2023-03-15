pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'pip install json'
        sh 'pip install requests'
        sh 'pip install datetime'
        sh 'python3 silence.py'
      }
    }
  }
}
