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
                curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
                curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
                echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check

                '''
                sh '''
                wget https://get.helm.sh/helm-v3.4.1-linux-amd64.tar.gz
                tar xvf helm-v3.4.1-linux-amd64.tar.gz
                rm helm-v3.4.1-linux-amd64.tar.gz
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
                kubectl version --client
                helm version

                '''

            }
        }
            stage('k8s'){
            when { anyOf { branch "master"; branch "dev" }}
        steps{
        sh'''
        systemctl start docker
        docker build -t d:0.0.1 ./
        docker run d:0.0.1
        curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
        systemctl docker start
        minikube start
        kubectl get po -A
        minikube kubectl -- get po -A
        minikube dashboard
        '''
        }}

        stage ('job1'){
            when { anyOf { branch "master"; branch "dev" }}
        steps{
        sh'''

        kubectl apply -f Jobs/job1.yaml
        sleep 10 #let postgrase to be up and running
        kubectl apply -f Jobs/job1-create-table.yaml
        '''

        }


    }


     stage ('job2'){
            when { anyOf { branch "master"; branch "dev" }}
        steps{
        sh'''
        aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 723653791098.dkr.ecr.us-east-1.amazonaws.com
        docker build -t bmc .
        docker tag bmc:latest 723653791098.dkr.ecr.us-east-1.amazonaws.com/bmc:latest
        docker push 723653791098.dkr.ecr.us-east-1.amazonaws.com/bmc:latest
        kubectl apply -f Jobs/job2.yaml

        '''
        }}
          stage ('job3'){
            when { anyOf { branch "master"; branch "dev" }}
        steps{
        sh'''
        aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 723653791098.dkr.ecr.us-east-1.amazonaws.com
        docker build -t bmc-job3 .
        docker tag bmc-job3:latest 723653791098.dkr.ecr.us-east-1.amazonaws.com/bmc-job3:latest
        docker push 723653791098.dkr.ecr.us-east-1.amazonaws.com/bmc-job3:latest
        kubectl apply -f Jobs/job3.yaml

        '''

        }}

}}
