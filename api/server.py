import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/health")
def hello():
    return "aibuildpack-api"

@app.route('/', methods = ['POST'])
def new_data():
    # CODE
    req = request.get_data()
    j = json.loads(req)
    return {
        "prediction" : j
    }