// // // pipeline {
// // //   agent any
// // // //   parameters {
// // // //     string(name: 'cluster_name', defaultValue: 'None', description: 'Enter the cluster name')
// // // //     string(name: 'region', defaultValue: 'None', description: 'Enter the region name in"jp tok" formate')
// // // //     string(name: 'API_token', defaultValue: 'None', description: 'Enter the api token of that region')
// // // //     string(name: 'duration_in_hours', defaultValue: 1.5, description: 'Enter the duration for the silencing')
// // // //   }
// // //   stages {
// // //     stage('silencing alert') {
// // //       steps {
// // //         sh 'python3 silencing_rule.py '
// // //       }
// // //     }
// // //      stage('sleep') {
// // //        steps {
// // //          sleep time: 60, unit: 'SECONDS' 
// // //        }
// // //      }
// // //      stage('crash') {
// // //        steps {
// // //          sh 'python3 crash.py'
// // //        }
// // //        post {
// // //          always {
// // //                sh 'python3 deleting_silencing_rule.py '
// // //                }
// // //            }
// // //     }
// // //      stage('deleting silencing rule') {
// // //        steps {
// // //          sh 'python3 deleting_silencing_rule.py '
// // //        }
// // //      }
// // //   }
  
// // // }

// // pipeline {
// //     parameters {
// //         string(name: 'INCREMENT_TIME', defaultValue: '4h', description: 'Enter the increment time (e.g., 4h)')
// //     }
    
// //     agent any
    
// //     stages {
// //         stage('Print Current Time') {
// //             steps {
// //                 script {
// //                     def (hours, minutes) = params.INCREMENT_TIME.findAll(/\d+|\D+/).findAll()
// //                     hours = hours.toInteger()
// //                     minutes = minutes.replace('h', '').toInteger()
                    
// //                     sh '''
// //                         #!/bin/bash
// //                         current_time=$(date "+%H:%M:%S")
// //                         incremented_time=$(date -d "$current_time + ${hours} hours ${minutes} minutes" "+%H:%M:%S")
// //                         echo "Current Time: $current_time"
// //                         echo "Incremented Time: $incremented_time"
// //                     '''
// //                 }
// //             }
// //         }
// //     }
// // }
// pipeline {
//     parameters {
//         string(name: 'INCREMENT_TIME', defaultValue: '4 hours', description: 'Enter the increment time (e.g., 4 hours)')
//     }
    
//     agent any
    
//     stages {
//         stage('Print Current Time') {
//             steps {
//                 script {
//                 def output = sh(script: 'python3 generate_output.py', returnStdout: true).trim()
//                 echo "Generated Output: ${output}"
//                  parameters {
//                       string(name: 'OUTPUT_PARAM', defaultValue: output, description: 'Generated output from Python script')
//                   }
//                 sh '''
//                     #!/bin/bash
//                     echo "Generated Output: ${params.OUTPUT_PARAM}"
//                     current_time=$(date "+%H:%M:%S")
//                 '''
//                 }
//             }
//         }
//     }
// }
pipeline {
    parameters {
        string(name: 'INCREMENT_TIME', defaultValue: '4 hours', description: 'Enter the increment time (e.g., 4 hours)')
    }
    
    agent any
    
    stages {
        stage('Print Current Time') {
            steps {
                script {
                    def output = sh(script: 'python3 generate_output.py', returnStdout: true).trim()
                    echo "Generated Output: ${output}"

                    // Define the output as a parameter
                    parameters {
                        string(name: 'OUTPUT_PARAM', defaultValue: output, description: 'Generated output from Python script')
                    }

                    sh '''
                        #!/bin/bash
                        echo "Generated Output: ${params.OUTPUT_PARAM}"
                        current_time=$(date "+%H:%M:%S")
                        echo "Current Time: $current_time"
                    '''
                }
            }
        }
    }
}


