from flask import Flask, jsonify, request
from flask_cors import CORS
from markupsafe import escape # Escape used to prevent injection via user input
from auth import accountCreate, accountLogin, getUserFromToken
from mongo_client import get_lab_by_name, get_professor_by_name

app = Flask(__name__)
# Eliminate CORS errors when making requests from front end
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



# Handle all Auth API endpoint routing
@app.route("/api/auth/<endpoint>", methods = ['POST'])
def auth_api_routing(endpoint):
    # Determine which endpoint the client is attempting to use
    match escape(endpoint):
        case "createaccount":
            try:
                content = request.get_json(silent=False)

                result = accountCreate(content['username'], content['password'], content['email'], content['role'])

                if result[0]:
                    responseData = {
                        "Success": True,
                        "Token": result[1]
                    }
                else:
                    responseData = {
                        "Success": False,
                        "SuccessMessage": "The server was unable to create the account!"
                    }
            except: 
                # Catch possible errors arising from invalid/no JSON being given
                responseData = {
                    "Success": False,
                    "SuccessMessage": "The server was unable to create the account! Check your JSON?"
                }
        case "login":
            try:
                content = request.get_json(silent=False)

                result = accountLogin(content['username'], content['password'])
                if result[0]:
                    # Returns JSON with token for the user.
                    responseData = {
                        "Success": True,
                        "Token": result[1]
                    }
                else:
                    # A token was not able to be created!
                    responseData = {
                        "Success": False,
                        "SuccessMessage": "The server was unable to log into the account!"
                    }
            except:
                # 
                responseData = {
                    "Success": False,
                    "SuccessMessage": "The server was unable to log into the account!"
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
            "SuccessMessage": "Please provide name query and ensure the endpoint exists"
        }
        return jsonify(responseData)

    # Sanitize the input
    name = escape(name)

    # Get Professor Data
    if target == "professor":
        dbData = get_professor_by_name(name)
        professorList = []

        # Convert the dictionary into a list so it can be JSONified
        if dbData is not None:
            for prof in dbData:
                professorList.append({
                    "Name": prof["Professor"],
                    "Position": prof["Position"],
                    "Email": prof["Email"],
                    "Phone": prof["Phone"],
                    "Office Location": prof["Office Location"],
                    "Homepage": prof["Homepage Link"]
                })

        responseData = {
            "Success": True,
            "Data": professorList
        }

        return jsonify(responseData)

    # Get Lab Data
    elif target == "lab":
        dbData = get_lab_by_name(name)
        labList = []

        # Convert the dictionary into a list so it can be JSONified
        if labList is not None:
            for lab in dbData:
                newData = {
                    "Name": lab["Labs"],
                    "Desc": lab["Description"],
                }

                # Some labs don't have staff listed so only attempt to add them if they are listed.
                if "Professors" in lab:
                    newData["Staff"] = lab["Professors"]
                
                labList.append(newData)

        responseData = {
            "Success": True,
            "Data": labList
        }
        return jsonify(responseData)

    # We weren't able to find our target so just return a Failure response.
    responseData = {
        "Success": False,
        "SuccessMessage": "Specified endpoint does not exist"
    }
    return jsonify(responseData)