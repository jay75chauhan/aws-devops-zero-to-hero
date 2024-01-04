# Create EKS using CLI

Please follow the prerequisites doc before this.

## Create using Fargate

```
eksctl create cluster --name demo-cluster --region ap-south-1 --fargate
```

## Delete the cluster

```
eksctl delete cluster --name demo-cluster --region ap-south-1
```



