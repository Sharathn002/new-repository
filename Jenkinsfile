pipeline {
  agent any
  stages {
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
    stage('crash') {
      steps {
        sh 'python3 crash.py'
      }
    }
    stage('disable silencing') {
      steps {
        sh 'python3 disable_silence.py'
      }
    }
  }
  post {
        always {
            stage('disable') {
                steps {
                  sh 'python3 disable_silence.py'                
                }
            }
        }
    }
}
