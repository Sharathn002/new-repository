// pipeline {
//   agent any
//   parameters {
//     string(name: 'cluster_name', defaultValue: 'None', description: 'Enter the cluster name')
//     string(name: 'region', defaultValue: 'None', description: 'Enter the region name in"jp tok" formate')
//     string(name: 'API_token', defaultValue: 'None', description: 'Enter the api token of that region')
//     string(name: 'duration_in_hours', defaultValue: 1.5, description: 'Enter the duration for the silencing')
//   }
//   stages {
//     stage('silencing alert') {
//       steps {
//         sh 'python3 silencing_rule.py ${params.cluster_name} ${params.region} ${params.API_token} ${params.duration_in_hours}'
//       }
//     }
// //     stage('sleep') {
// //       steps {
// //         sleep time: 60, unit: 'SECONDS' 
// //       }
// //     }
// //     stage('crash') {
// //       steps {
// //         sh 'python3 crash.py'
// //       }
// //       post {
// //         always {
// //               sh 'python3 deleting_silencing_rule.py ${params.cluster_name} ${params.region} ${params.API_token} ${params.duration_in_hours}'
// //               }
// //           }
//     }
// //     stage('deleting silencing rule') {
// //       steps {
// //         sh 'python3 deleting_silencing_rule.py ${params.cluster_name} ${params.region} ${params.API_token} ${params.duration_in_hours}'
// //       }
// //     }
// //   }
  
// }
pipeline {
  agent any
  
  parameters {
    string(name: 'region', defaultValue: 'Jp tok', description: 'Enter the region')
    string(name: 'api_token', defaultValue: '3e91771e-40d2-42cd-96ac-ebe08462c96c', description: 'Enter the api token')
    string(name: 'cluster_name', defaultValue: 'webapCluster/cfvdf6ef0lb6gpb1puig', description: 'Enter the cluster name')
//     booleanParam(name: 'FLAG', defaultValue: true, description: 'Select flag')
//     choice(name: 'CHOICE', choices: ['Option A', 'Option B', 'Option C'], description: 'Select an option')
  }

  stages {
    stage('Run Python Script') {
      steps {
        sh "python3 my_script.py ${params.region} ${params.api_token} ${params.cluster_name}"
      }
    }
  }
}

