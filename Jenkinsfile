// Jenkins env var reference https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#working-with-your-jenkinsfile

pipeline {
    agent { label '' }

    stages {
        stage("install ansible") {
            when { anyOf { branch "master"; branch "dev" }}
            steps {
                sh '''
                echo 'hi'
                '''
            }

        }


    }
}