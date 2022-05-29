# Description of the SRE PLATFORM APP
The team SRE Platform has created a Kubernetes cluster and the first few services have been deployed to it. Now this app
exposes some information on the current state of each service. There are two APIs exposed in this service. THe service is deployed in the kubernetes.

## Required softwares
- kubectl client version "v1.24.0"
- minikube version: v1.25.2
- Python 3.8.10
- Flask 2.1.2
- Docker version 20.10.7


## Steps to run the application
- Use a linux(Ubuntu 20.04.2 LTS) for development
- Install all softwares mentioned above
- Clone the repository : git clone https://github.com/iamrachanagupta/sre-platform-applicant-test.git
- Create a docker image
- Deploy docker image to kubernetes as a service.
- Check if your app pod is in running state : kubectl get pods
- Go to browser and check for the APIs exposed


## Docker commands 
Go to utilapp folder
- To create docker image: ` docker image build -t sre-platform-app . `
- To run the docker container: ` docker run -d -p 5000:5000 sre-platform-app `
- To login to the docker container: ` docker exec -it <container_id> bash `

## Commands to deploy the application in kubernetes
    
Go to sre-platform-applicant-test folder: This is our application folder

```
kubectl apply -f service.yaml
kubectl apply -f deployment.yaml
kubectl create rolebinding default-view \
  --clusterrole=view \
  --serviceaccount=default:default \
  --namespace=default
kubectl get pods -n default           -----> SHOULD SHOW YOUR APP IN RUNNING STATE ALONG WITH EXISTING PODS
kubectl get svc -n default
kubectl get deployment -n default
```
        
## To get sre-platform-app container
` docker container ls | grep k8s_sre-platform-app `


## To restart a pod
` kubectl rollout restart deployment sre-platform-app-deployment -n default `


## To grant access to the pod to access other pods in the same namespace
```
kubectl create rolebinding default-view \
  --clusterrole=view \
  --serviceaccount=default:default \
  --namespace=default
```
 
 
### References
    https://thenewstack.io/kubernetes-access-control-exploring-service-accounts/
    Github link: https://github.com/iamrachanagupta/sre-platform-applicant-test
