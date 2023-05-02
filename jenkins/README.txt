curretly minikube does not create token for the service account so:
1) create jenkins-service-token.yaml file
2) apply the jenkins-service-token.yaml
3) SECRET_NAME="jenkins-token" ----> where the jenkins-token is the name of the token from the file
4) TOKEN=$(kubectl get secret ${SECRET_NAME} -n devops-tools -o jsonpath='{$.data.token}' | base64 -d | sed $'s/$/\\\n/g')
5) set the token in the jekins gui when suting up the kubenetes cloud : https://devopscube.com/jenkins-build-agents-kubernetes/
6) in order to log in to container and verify you could run kubectl: kubectl exec -it bibi-web-app-s4w8d-13qhc    -n devops-tools    -c inbound-agent  -- /bin/bash
7) in order to perform deployment in another name space there is workaround which give admin permission: kubectl create clusterrolebinding serviceaccounts-cluster-admin --clusterrole=cluster-admin --group=system:serviceaccounts
