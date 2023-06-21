in this task we create 2 deploymrnt - one for the mongo db with clusterIP service which the bibi-web-app will connct to. and a web app deployment which connect to the mongodb pod
in order to install and run the following:
1) kubectl apply -f mongodb-deployment.yaml
2) kubectl apply -f bibi_web_server_ex1.yaml
3) run a mongodb client to see that you can connect to mongodb: kubectl run -it --rm --image=bibiefrat/ci-cd-1:my-mongo --restart=Never mongo-client -- /bin/bash (and inside: mongosh  --host mongo:27017 --username bibi --password 029365947)
4) see the log in thew web app that it managed to connect to monogodb:
4.1) kubectl get pods
4.2) kubectl logs <web-app pod id>



here we use secret from aws secret manager. we crreate the secret using:


aws --region "$REGION" secretsmanager  create-secret --name mongo-creds --secret-string '{"username":"YmliaQ==", "password":"MDI5MzY1OTQ3"}'
{
    "VersionId": "c6955a33-0ab9-46d6-8405-6a0f2c9fc04d",
    "Name": "mongo-creds",
    "ARN": "arn:aws:secretsmanager:eu-west-1:019273956931:secret:mongo-creds-e3oUcA"
}


in order to use secret manager from within eks (k8s) - we need to ceate the following IAM role - assign it to k8s "service account" - and assign the service account to a pod - so the pod can assume the
secret and mount the secret as volume.

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::019273956931:oidc-provider/oidc.eks.eu-west-1.amazonaws.com/id/6161709AAED58895804AB964E1F10D3B"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "oidc.eks.eu-west-1.amazonaws.com/id/6161709AAED58895804AB964E1F10D3B:sub": "system:serviceaccount:bibi-ns:secret-manager-service-account",
                    "oidc.eks.eu-west-1.amazonaws.com/id/6161709AAED58895804AB964E1F10D3B:aud": "sts.amazonaws.com"
                }
            }
        }
    ]
}

in the above role we see that Principal is the EKS cluster - "oidc.eks.eu-west-1.amazonaws.com" (specific in the cluster is the secret-manager-service-account - my created service account - which can assume the role)
the role give the following permissions (which give the pod permissions to GetSecretValue, DescribeSecret):

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret"
            ],
            "Resource": [
                "arn:aws:secretsmanager:eu-west-1:019273956931:secret:mongo-creds-e3oUcA"
            ]
        }
    ]
}

the above Princiapl is eks and  is federated since k8s and aws have different authorization mechanism(eks does not work with IAM) - so in order for eks cluster to work with aws IAM authorization mechanism we
nee to federate the permissions using IAM (to the EKS) ---> so entities inside the cluster (like pod) will be able to use aws services (which use IAM authentication)

create the above policy - with cli
POLICY_ARN=$(aws --region "$REGION" --query Policy.Arn --output text iam create-policy --policy-name eks-deployment-policy --policy-document '{     "Version": "2012-10-17",     "Statement": [ {         "Effect": "Allow",         "Action": ["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"],         "Resource": ["arn:aws:secretsmanager:eu-west-1:019273956931:secret:mongo-creds-e3oUcA"]     } ] }')

create IAM service account for the above policy with cli:
eksctl create iamserviceaccount --name secret-manager-service-account --region="$REGION" --cluster "$CLUSTERNAME" --attach-policy-arn "$POLICY_ARN" --approve --override-existing-serviceaccounts --namespace bibi-ns