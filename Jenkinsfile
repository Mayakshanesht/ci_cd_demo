pipeline{
    agent any
    environment{
        DOCKERHUB_USER = "mayakshanesht"
        DOCKER_IMAGE = "calculator"
    }
    stages{
        stage('Checkout'){
            steps{
                git branch:'main' url:'https://github.com/Mayakshanesht/ci_cd_demo.git'
            }
        }
        stage('Build Docker Image'){
            steps{
                sh docker build -t $DOCKER_IMAGE .
            }
        }

        stage('Push Image to Docker Hub'){
            steps{
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy to Kubernetes'){
            steps{
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}