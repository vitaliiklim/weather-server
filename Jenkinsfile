pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'git@github.com:vitaliiklim/weather-server.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv  # створення віртуального середовища
                    . venv/bin/activate && pip install --upgrade pip  # активація та оновлення pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt  # установка залежностей
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest  # запуск тестів
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/test-results/*.xml', allowEmptyArchive: true
            echo 'Some tests failed.'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}
