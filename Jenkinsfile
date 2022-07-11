pipeline {
    agent { label 'ec2-fleet' }

    stages {
        stage('Build Simple WebServer') {
            when { anyOf { branch "master"; branch "dev" }}
            steps {
                echo 'Building..'
                sh '''
                docker build -t hello-world .
                '''
            }

        }}}