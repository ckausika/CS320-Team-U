# The flask server can be ran with the following commands:
#
# .venv\Scripts\activate
# flask --app app run
#

from flask import Flask, jsonify, request
from markupsafe import escape # escape used to prevent injection via user input

app = Flask(__name__)

# Handle all Auth API endpoint routing
@app.route("/api/auth/<endpoint>")
def auth_api_routing(endpoint):
    responseData = {
        "Success": False,
        "Endpoint used": escape(endpoint)
    }

    return jsonify(responseData)


# Handle all Get API endpoint routing
@app.route("/api/get/<endpoint>")
def get_api_routing(endpoint):
    target = escape(endpoint)
    name = request.args.get('name') # Name of either the lab or professor

    # If the required name query doesn't exist than just return a Failure response
    if name is None:
        responseData = {
            "Success": False,
        }
        return jsonify(responseData)

    # Get Professor Data
    if target == "professor":
        responseData = {
            "Success": True,
            "Endpoint used": escape(endpoint) + " - query: " + name
        }
        return jsonify(responseData)

    # Get Lab Data
    elif target == "lab":
        responseData = {
            "Success": True,
            "Endpoint used": escape(endpoint) + " - query: " + name
        }
        return jsonify(responseData)

    # We weren't able to find our target so just return a Failure response.
    responseData = {
        "Success": False,
    }
    return jsonify(responseData)