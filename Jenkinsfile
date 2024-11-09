pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/vitaliiklim/weather-server.git', branch: 'main'
            }
        }
        
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '. venv/bin/activate && pip install --upgrade pip --break-system-packages'
                sh '. venv/bin/activate && pip install -r requirements.txt --break-system-packages'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/test-results.xml', allowEmptyArchive: true
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}
