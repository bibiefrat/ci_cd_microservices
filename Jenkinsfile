pipeline {
  options {
    buildDiscarder(logRotator(daysToKeepStr: '1', numToKeepStr: '3'))
    disableConcurrentBuilds()
    timestamps()
    timeout(time: 10, unit: 'MINUTES')
  }
  agent {
    kubernetes {
      label 'bibi-web-app'
      idleMinutes 5
      yamlFile 'jenkins_k8s.yaml'
      defaultContainer 'jnlp'
}
   }
  stages {
    stage('Build') {
      steps {
        container('maven') {
          sh """
            pwd
            """
        }
      }
    }
    stage('Test') {
      steps {
        container('maven') {
          sh """
             ls -ltr
          """
        }
      }
    }
    stage('Push') {
      steps {
        container('docker') {
          sh """
             docker ps -a
          """
        }//container
      }//steps
    }//stage
    stage('Deploy') {
      steps {
        container('inbound-agent') {
          withKubeConfig([namespace: "demo_app"]) {
              sh """
                 kubectl apply -f bibi_web_server_ex1.yaml -n demo_app
                 sleep 30
              """
          }//withKubeConfig
        }//container
      }//steps
    }//stage
    stage('Remove Deployment') {
      steps {
        container('inbound-agent') {
          withKubeConfig([namespace: "demo_app"]) {
              sh """
                 kubectl delete -f bibi_web_server_ex1.yaml -n demo_app
              """
          }//withKubeConfig
        }//container
      }//steps
    }//stage
  }
}