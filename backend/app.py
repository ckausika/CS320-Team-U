# Server can be ran with command: flask --app app run

from flask import Flask
from markupsafe import escape # escape used to prevent injection via user input

app = Flask(__name__)

# Handle all Auth API endpoint routing
@app.route("/api/auth/<endpoint>")
def auth_api_routing(endpoint):
    return f'<p>Endpoint: {escape(endpoint)} is being served</p>'