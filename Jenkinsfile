pipeline {
    agent any 
    stages {
        stage('git chekout') {
            steps {
                // below command pull file from github and insert in  /var/lib/jenkins/workspace
               git branch: 'main', credentialsId: 'barmaiyadevu', url: 'https://github.com/barmaiyadevu/dags.git'
            }
        }
                

        stage('connect airflow server and coppy file') {
            steps {
                sshagent(['airflow']) {
                     sshPublisher(publishers: [sshPublisherDesc(configName: 'airflow', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '.', remoteDirectorySDF: false, sourceFiles: '*.*')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                     
                }
            }
        }
        

    }
}
