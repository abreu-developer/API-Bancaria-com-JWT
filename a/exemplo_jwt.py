"""

from flask import Flask, jsonify, request
import jwt
from datetime import datetime, timedelta, timezone


app = Flask(__name__)


@app.route("/", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            "exp": datetime.now(timezone.utc) + timedelta(minutes=10),
            "email": "jjjjj@gmail.com"
        },
        key="minhaChave",
        algorithm="HS256"
    )

    return jsonify({"token": token}), 200


@app.route("/secret", methods=["POST"])
def segredo(): 
    raw_tokens = request.headers.get("authorization")
    token = raw_tokens.split()[1]
    try:
        token_info = jwt.decode(token,key="minhaChave", algorithms="HS256" )
        return jsonify({"ola": "segredo"}), 200
    except Exception as exception:
        return jsonify({"error": str(exception)}),400


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3000,
        debug=True
    )
    
"""
