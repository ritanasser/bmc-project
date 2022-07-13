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
                             sh'''
                sudo apt-get update
                sudo apt-get install docker.io
                docker ––version
                sudo systemctl enable docker
                sudo systemctl status docker
                sudo systemctl start docker
                curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
                sudo apt-get install curl
                sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
                sudo apt-get install kubeadm kubelet kubectl
                sudo apt-mark hold kubeadm kubelet kubectl
                kubeadm version
                '''
            }

        }
         stage('Test') {
            when { changeRequest() }
            steps {
                echo 'Testing..'
                sh '''
                ansible --version
                python3 -m pip show ansible
                '''

            }
        }


    }
}