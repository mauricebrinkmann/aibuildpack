import os
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

if __name__ == "__main__":
    if os.environ.get('VCAP_SERVICES') is None: # running locally
        PORT = 8080
        DEBUG = True
    else:                                       # running on CF
        PORT = int(os.getenv("PORT"))
        DEBUG = False

    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
