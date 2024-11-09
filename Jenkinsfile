pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv' // створення віртуального середовища
                sh '. venv/bin/activate && pip install --upgrade pip' // оновлення pip в середовищі
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '. venv/bin/activate && pip install -r requirements.txt' // встановлення залежностей
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest' // запуск тестів
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
