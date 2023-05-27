in this task we create 2 deploymrnt - one for the mongo db with clusterIP service which the bibi-web-app will connct to. and a web app deployment which connect to the mongodb pod
in order to install and run the floowing:
1) kubectl apply -f mongodb-deployment.yaml
2) kubectl apply -f bibi_web_server_ex1.yaml
3) run a mongodb client to see that you can connect to mongodb: kubectl run -it --rm --image=bibiefrat/ci-cd-1:my-mongo --restart=Never mongo-client -- /bin/bash (and inside: mongosh  --host mongo:27017 --username bibi --password 029365947)
4) see the log in thew web app that it managed to connect to monogodb:
4.1) kubectl get pods
4.2) kubectl logs <web-app pod id>