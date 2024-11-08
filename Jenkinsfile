pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                git url: 'git@github.com:vitaliiklim/weather-server.git', credentialsId: '5f728f2f-8b17-4538-8e04-e9eb923d48f5'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Створення віртуального середовища
                sh 'python3 -m venv venv'
                
                // Активація середовища та встановлення залежностей
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && python -m unittest discover tests'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
            echo 'Some tests failed.'
        }
    }
}

