pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python and Pip') {
            steps {
                sh '''
                    python3 --version
                    venv/bin/pip --version
                '''
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv  # створення віртуального середовища
                    venv/bin/pip install --upgrade pip  # оновлення pip в середовищі
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    venv/bin/pip install -r requirements.txt  # встановлення залежностей
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    venv/bin/pytest  # запуск тестів
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
            echo 'Some tests failed.'
        }
    }
}1~pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python and Pip') {
            steps {
                sh '''
                    python3 --version
                    venv/bin/pip --version
                '''
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv  # створення віртуального середовища
                    venv/bin/pip install --upgrade pip  # оновлення pip в середовищі
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    venv/bin/pip install -r requirements.txt  # встановлення залежностей
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    venv/bin/pytest  # запуск тестів
                '''
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
