pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vitaliiklim/weather-server.git'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'          // створення віртуального середовища
                sh '. venv/bin/activate'           // активація віртуального середовища
            }
        }
        stage('Install Dependencies') {
            steps {
                // Виконуємо встановлення pip і залежностей у віртуальному середовищі
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/'  // Запуск тестів
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
