pipeline {
    agent any

    environment {
        PYTHON = 'python'  // En Windows, normalmente se llama python, no python3
    }

    stages {
        stage('Build') {
            steps {
                echo 'Compilando el proyecto...'
                bat "${PYTHON} -m py_compile validador_seguridad_app.py"
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                bat "${PYTHON} -m unittest test_app.py"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando aplicación en entorno local (simulación)...'
                echo 'Despliegue completado exitosamente.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado con éxito.'
        }
        failure {
            echo 'Error en el pipeline.'
        }
    }
}
