pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker-compose up -d'
                sh 'sleep 10' // Give some time for services to start
                sh 'curl http://localhost:5001'
                sh 'curl http://localhost:5002'
                sh 'curl http://localhost:5003'
                sh 'docker-compose down'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying... (This is a placeholder for actual deployment steps)'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}