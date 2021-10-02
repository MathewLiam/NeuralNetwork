pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('Lint') {
            steps {
                sh 'pylint --rcfile=pylintrc $(find . -iname "*.py")'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m coverage run --rcfile=.coveragerc -m unittest discover -s src -p "*_spec.py" --verbose -b'
                sh 'python -m coverage html --rcfile=.coveragerc'
            }
        }
        stage('Build') {
            steps {
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m build --sdist'
                sh 'python -m build --wheel'
            }
        }
        stage('publish') {
            steps {
                sh 'python -m twine upload -u ${PYPI_USERNAME} -p ${PYPI_API_TOKEN} dist/*'
            }
        }
    }
}
