from utilModel import utilModels
from flask import Flask, jsonify

app = Flask(__name__)


global utils_obj
@app.before_first_request
def initialize_all_utils():
    global utils_obj
    utils_obj = utilModels()


@app.route("/")
def hello():
    return "Hello from Python!"

@app.route("/services")
def getServices():
    return jsonify(utils_obj.get_all_services())

@app.route("/services/<applicationGroup>")
def getServicesByAppGrp(applicationGroup):
    return "Services by appl Group!"



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
