pipeline {
  agent any
  stages {
    stage('silencing alert') {
      steps {
        sh 'python3 silencing_rule.py'
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
      post {
        always {
              sh 'python3 deleting_silencing_rule.py'
              }
          }
    }
    stage('deleting silencing rule') {
      steps {
        sh 'python3 deleting_silencing_rule.py'
      }
    }
  }
  
}
