pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\hjf\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Syntax Check') {
            steps {
                bat '"C:\\Users\\hjf\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-management .'
            }
        }

    }
}