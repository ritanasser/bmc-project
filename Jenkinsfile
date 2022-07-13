// Jenkins env var reference https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#working-with-your-jenkinsfile

pipeline {
    agent { label '' }

    stages {
        stage("Building") {
            when { anyOf { branch "master"; branch "dev" }}

            steps {

                sh '''
                python3 -m pip -V
                python3 -m pip install --user ansible
                python3 -m pip install --upgrade --user ansible





                '''
            }

        }
         stage('Test') {
            when { changeRequest() }
            steps {
                echo 'Testing..'
                sh ' ansible --version
                python3 -m pip show ansible'
            }
        }


    }
}