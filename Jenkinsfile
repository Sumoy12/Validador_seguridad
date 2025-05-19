pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/tu_usuario/tu_repositorio.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Instala Python si no está instalado o asegúrate que esté en PATH
                bat 'python --version'  // para Windows
                // Instala unittest no necesita, es parte de la librería estándar
                // Si usas paquetes extras, acá iría el pip install
            }
        }

        stage('Run Tests') {
            steps {
                // Ejecuta las pruebas unitarias
                bat 'python -m unittest test_validador.py'
            }
        }

        stage('Build') {
            steps {
                echo 'No aplica build para este proyecto Python simple'
            }
        }

        stage('Deploy') {
            steps {
                echo 'No hay despliegue para este proyecto, pero puedes agregar pasos si tienes'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado con éxito'
        }
        failure {
            echo 'Pipeline falló'
        }
    }
}
