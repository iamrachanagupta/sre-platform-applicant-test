from utilModel import utilModels
from flask import Flask, jsonify

app = Flask(__name__)


global utils_obj
@app.before_first_request
def initialize_all_utils():
    global utils_obj
    utils_obj = utilModels()


@app.route("/")
def welcome():
    return "WELCOME TO THE SRE PLATFORM APP"



'''
Expose information on all pods in the cluster
Add an endpoint to the service that exposes the number of pods running in the cluster in namespace `default` per service
and per application group:

```
GET `/services`
[
  {
    "name": "<service>",
    "applicationGroup": "alpha",
    "runningPodsCount": 2
  },
  {
    "name": "<service>",
    "applicationGroup": "beta",
    "runningPodsCount": 1
  },
  ...
]
```
'''
@app.route("/services")
def getServices():
    return jsonify(utils_obj.get_all_services())


'''
Expose information on a group of applications in the cluster

Create an endpoint in your service that exposes the pods in the cluster in namespace `default` that are part of the same `applicationGroup`:

```
GET `/services/{applicationGroup}`
[
  {
    "name": "<service>",
    "applicationGroup": "<applicationGroup>",
    "runningPodsCount": 1
  },
  ...
]
```
'''
@app.route("/services/<applicationGroup>")
def getServicesByAppGrp(applicationGroup):
    return jsonify(utils_obj.get_all_services_by_appGrp(applicationGroup))



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
