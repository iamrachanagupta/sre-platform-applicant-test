## Docker commands 
    Go to utilapp folder
        docker image build -t sre-platform-app .
        docker run -d -p 5000:5000 sre-platform-app


## To get sre-platform-app container
    > docker container ls | grep k8s_sre-platform-app

## To restart a pod
    > kubectl rollout restart deployment sre-platform-app-deployment -n default

## To grant access to the pod to access other pods in the same namespace
    kubectl create rolebinding default-view \
      --clusterrole=view \
      --serviceaccount=default:default \
      --namespace=default

### References
    https://thenewstack.io/kubernetes-access-control-exploring-service-accounts/

