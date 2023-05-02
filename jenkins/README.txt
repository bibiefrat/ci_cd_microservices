curcurrently minikube does not create token for the service account so:
1) create jenkins-service-token.yaml file (under jenkins dir)
2) apply the jenkins-service-token.yaml
3) SECRET_NAME="jenkins-token" ----> where the jenkins-token is the name of the token from the file
4) TOKEN=$(kubectl get secret ${SECRET_NAME} -n devops-tools -o jsonpath='{$.data.token}' | base64 -d | sed $'s/$/\\\n/g')
5) set the above token in the jekins gui when setting up the kubenetes cloud : https://devopscube.com/jenkins-build-agents-kubernetes/ ----> this is the credential in the wizard
in order to log in to container and verify you could run kubectl: kubectl exec -it <jenkins pod created>   -n devops-tools    -c inbound-agent  -- /bin/bash
in order to perform deployment in another name space (if we want the jenkins k8s agent to deploy inside k8s our private deployment) there is workaround which give admin permission to all k8s users : kubectl create clusterrolebinding serviceaccounts-cluster-admin --clusterrole=cluster-admin --group=system:serviceaccounts
