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
                
                // Переконатися, що pip у віртуальному середовищі оновлено
                sh './venv/bin/pip install --upgrade pip'
                
                // Активація середовища та встановлення залежностей
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Запуск тестів у віртуальному середовищі
                sh './venv/bin/python -m unittest discover tests'
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

