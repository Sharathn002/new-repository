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
        sh 'pip install requests'
        sh 'python3 add.py'
      }
    }
  }
}
