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
    stage('silencing alert') {
      steps {
        sh 'python3 Silencing.py'
      }
    }
    stage('sleep') {
      steps {
        sleep time: 60, unit: 'SECONDS' 
      }
    }
    stage('disable silencing') {
      steps {
        sh 'python3 disable_silence.py'
      }
    }
  }
}
