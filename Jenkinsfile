
pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub_credentials'  // ID des credentials DockerHub dans Jenkins
        DOCKER_IMAGE = 'vareladavidhugo/my_python_app:latest'  // Remplace par ton repository DockerHub
    }

    stages {
        stage('Cloner le dépôt') {
            steps {
                git branch: 'main', url: 'https://github.com/VARELAdavidhugo/projet_python.git'
            }
        }

        stage('Installer les dépendances') {
            steps {
                sh '''
                    python -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Exécuter les tests unitaires') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest --junit-xml test-reports/results.xml tests/
                '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Construire l’image Docker') {
            steps {
                script {
                    echo "Construction de l'image Docker : ${DOCKER_IMAGE}"
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Pousser l’image sur DockerHub') {
            steps {
                script {
                    docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }
    }
}
