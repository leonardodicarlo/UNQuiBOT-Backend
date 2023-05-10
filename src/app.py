
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

import sys
import re
sys.path.append("")

app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    cookieLogin = request.get_json().get("login")
    userLogged = int(cookieLogin.split("=")[1])

    response = get_response(text, userLogged)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)