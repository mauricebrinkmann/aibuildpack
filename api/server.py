import os
import sys
import json
from flask import Flask
from flask import request
from prediction import Prediction

app = Flask(__name__)
prediction = ""
aijson = ""

@app.route("/model")
def hello():
    return json.dumps(aijson)

@app.route("/health")
def hello():
    return "aibuildpack-api"

@app.route('/', methods = ['POST'])
def new_data():
    # CODE
    req = request.get_data()
    input = json.loads(req)
    target = prediction.get_prediction(input)
    return {
        "prediction" : json.dumps(target)
    }

if __name__ == "__main__":
    aijson = json.load(sys.stdin)
    prediction = Prediction(aijson)
    if os.environ.get('VCAP_SERVICES') is None: # running locally
        PORT = 8080
        DEBUG = True
    else:                                       # running on CF
        PORT = int(os.getenv("PORT"))
        DEBUG = False

    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)

