# The flask server can be ran with the following commands:
#
# python -m venv backend/.venv
# cd backend
# pip install -r requirements.txt
# .venv\Scripts\activate
# flask --app app run
#

from flask import Flask, jsonify, request, Response
from markupsafe import escape # escape used to prevent injection via user input
from auth import accountCreate

app = Flask(__name__)

#  {
#      Status: "Success"
#  }, 200


# Status Endpoint
@app.route("/")
def statusEndpoint():
    responseData = {
        "Status": "Success"
    }
    
    return jsonify(responseData), 200

    #return Response(responseData, mimetype='application/json', status=200, headers={"Access-Control-Allow-Origin": "*"})

# Handle all Auth API endpoint routing
@app.route("/api/auth/<endpoint>")
def auth_api_routing(endpoint):
    # If the request is not a POST request then do not serve it
    if request.method != 'POST':
        responseData = {
                "Success": False,
                "SuccessMessage": "The request is not a POST request!"
            }
        return jsonify(responseData)
    
    # Determine which endpoint the client is attempting to use
    match escape(endpoint):
        case "createaccount":
            result = accountCreate(request.form['username'], request.form['password'])

            if result:
                print("blah")
            else:
                responseData = {
                    "Success": False,
                    "SuccessMessage": "The server was unable to create the account!"
                }
        case _:
            # The endpoint does not exist
            responseData = {
                "Success": False,
                "SuccessMessage": f'Unable to handle endpoint: {escape(endpoint)}! Is the endpoint spelled properly?',
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