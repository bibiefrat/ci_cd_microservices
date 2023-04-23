in order to install and run the chart:
1) cd <charm root directory : "bibi-web-app-chart">
2) helm package .   ----->  will create "bibi-web-app-chart-0.1.0.tgz"
3) helm install bibi-web-app-helm bibi-web-app-chart-0.1.0.tgz   ---> will install the package in minikube k8s
4) helm ls ---> see all releases
5) helm delete bibi-web-app-helm  --> will remove the helm from the minikibe and delete this relese - in order to reinstall ---> helm install bibi-web-app-helm bibi-web-app-chart-0.1.0.tgz