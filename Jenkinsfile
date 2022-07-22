// Jenkins env var reference https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#working-with-your-jenkinsfile

pipeline {
    agent any
    environment{
    DockerURL ='723653791098.dkr.ecr.us-east-1.amazonaws.com'
    }

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
            stage('docker'){
            when { anyOf { branch "master"; branch "dev" }}
        steps{
        sh'''
        IMAGE="bmc-docker:${BRANCH_NAME}_${BUILD_NUMBER}"
        docker login -u AWS https://723653791098.dkr.ecr.us-east-1.amazonaws.com -p $(aws ecr get-login-password --region us-east-1)
        docker build -t ${IMAGE} .
        docker tag ${IMAGE} ${DockerURL}/${IMAGE}
        docker push ${DockerURL}/${IMAGE}



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
        IMAGE="bmc-docker:${BRANCH_NAME}_${BUILD_NUMBER}"
        docker login -u AWS https://723653791098.dkr.ecr.us-east-1.amazonaws.com -p $(aws ecr get-login-password --region us-east-1)
        docker build -t ${IMAGE} .
        docker tag ${IMAGE} ${DockerURL}/${IMAGE}
        docker push ${DockerURL}/${IMAGE}
        kubectl apply -f Jobs/job2.yaml

        '''
        }}
          stage ('job3'){
            when { anyOf { branch "master"; branch "dev" }}
        steps{
        sh'''
        IMAGE="bmc-docker:${BRANCH_NAME}_${BUILD_NUMBER}"
        docker login -u AWS https://723653791098.dkr.ecr.us-east-1.amazonaws.com -p $(aws ecr get-login-password --region us-east-1)
        docker build -t ${IMAGE} .
        docker tag ${IMAGE} ${DockerURL}/${IMAGE}
        docker push ${DockerURL}/${IMAGE}
        kubectl apply -f Jobs/job3.yaml

        '''

        }}
          stage ('job4'){
            when { anyOf { branch "master"; branch "dev" }}
        steps{
        sh'''
        IMAGE="bmc-docker:${BRANCH_NAME}_${BUILD_NUMBER}"
        docker login -u AWS https://723653791098.dkr.ecr.us-east-1.amazonaws.com -p $(aws ecr get-login-password --region us-east-1)
        docker build -t ${IMAGE} .
        docker tag ${IMAGE} ${DockerURL}/${IMAGE}
        docker push ${DockerURL}/${IMAGE}
        kubectl apply -f Jobs/job4.yaml
        kubectl delete -f Jobs/job4.yaml

        '''

        }}
          stage ('helm'){
            when { anyOf { branch "master"; branch "dev" }}
        steps{
        sh'''
        IMAGE="bmc-docker:${BRANCH_NAME}_${BUILD_NUMBER}"
        docker login -u AWS https://723653791098.dkr.ecr.us-east-1.amazonaws.com -p $(aws ecr get-login-password --region us-east-1)
        docker build -t ${IMAGE} .
        docker tag ${IMAGE} ${DockerURL}/${IMAGE}
        docker push ${DockerURL}/${IMAGE}
        wget https://get.helm.sh/helm-v3.4.1-linux-amd64.tar.gz
        tar xvf helm-v3.4.1-linux-amd64.tar.gz
        helm version
        helm repo add fluent https://fluent.github.io/helm-charts
        helm repo update
        helm show values fluent/fluentd
        kubectl get nodes
        kubectl delete node
        helm del fluent


        '''

        }}

}}
