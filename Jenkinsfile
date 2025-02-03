pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "mayakshanesht"
        DOCKER_IMAGE = "LLM-APP"
        // DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        // KUBECONFIG = credentials('kubeconfig')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Mayakshanesht/ci_cd_demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_USER/$DOCKER_IMAGE .'  // Fix shell command syntax
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push $DOCKERHUB_USER/$DOCKER_IMAGE'  // Fix Docker push command
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh """
                        sudo kubectl apply -f deployment.yaml
                    """
                }
            }
        }
    }
}