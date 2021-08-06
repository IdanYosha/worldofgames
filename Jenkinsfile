

pipeline {
    agent any

    stages {
        stage ('#1 Git checkout') {
            steps {
                git branch: 'master',
                credentialsId: 'idanyosha',
                url: 'https://github.com/IdanYosha/worldofgames.git'
                }
        }
        stage ('#2 Build Dockerfile') {
            steps {
                bat 'docker build -t worldofgames .'

                }
        }
        stage ('#3 run Dockerfile') {
            steps {
                bat 'docker run --name games-container -d -t -p 8777:80 worldofgames'

                }
        }
        stage ('#4 run tests') {
            steps {
                bat 'docker exec -t -d games-container python /MainScores.py'
                bat 'docker exec -t -d games-container python /tests/e2e.py'
               }
        }   
        stage ('#5 stop and delete containers') {
            steps {
                bat 'docker stop games-container'
                bat 'docker rm games-container'
				bat 'docker push idanyosha/worldofgames'
                }
        }   
            
            
            
    }
}
