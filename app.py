from flask import Flask, request

import json

app = Flask(__name__)

global_controller_data = {}
global_esp32_data = {}

@app.route("/")
def home():
    return "Reflector Rest API", 200

# @app.route("/receive_controller", methods=["GET", "POST"])
# def receive_controller():
#     global global_controller_data
#     global_controller_data = json.loads(request.data)
#     return "done", 200
    
# @app.route("/emit_controller", methods=["GET", "POST"])
# def emit_controller():  
#     global global_controller_data
#     return global_controller_data

# @app.route("/receive_esp32", methods=["GET", "POST"])
# def receive_esp32():
#     global global_esp32_data
#     global_esp32_data = json.loads(request.data)
#     return global_esp32_data

# @app.route("/emit_esp32", methods=["GET", "POST"])
# def emit_esp32():
#     global global_esp32_data
#     return global_esp32_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)