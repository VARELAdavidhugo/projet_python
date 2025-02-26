pipeline {
    agent any

    stages {
        stage('Cloner le dépôt') {
            steps {
                git branch: 'main', url: 'https://github.com/VARELAdavidhugo/projet_python.git'
            }
        }

        stage('Exécuter un test simple') {
            steps {
                echo 'Jenkinsfile trouvé et exécuté avec succès !'
            }
        }
    }
}
