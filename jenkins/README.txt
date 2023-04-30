curretly minikube does not create token for the service account so:
1) create jenkins-service-token.yaml file
2) apply the jenkins-service-token.yaml
3) SECRET_NAME="jenkins-token" ----> where the jenkins-token is the name of the token from the file
4) TOKEN=$(kubectl get secret ${SECRET_NAME} -n devops-tools -o jsonpath='{$.data.token}' | base64 -d | sed $'s/$/\\\n/g')
5) set the token in the jekins gui when suting up the kubenetes cloud : https://devopscube.com/jenkins-build-agents-kubernetes/