import requests 
from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Emperor Investments!"

@app.route("/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    app.logger.debug(f"Received code: {code}")  # Log the received code
    if code:
        data = {
            "client_id": "vd46TdQP",
            "client_secret": "4ddeaa34-c192-4154-85e1-9211266bd663",
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": "https://emperor-investments.vercel.app/callback"
        }
        try:
            response = requests.post("https://api.smartapi.angelbroking.com/oauth2/token", data=data)
            app.logger.debug(f"API response: {response.status_code} - {response.text}")  # Log full response status and body
            if response.status_code == 200:
                return jsonify(response.json())
            else:
                app.logger.error(f"API Error: {response.text}")  # Log detailed error
                return jsonify({"error": "Failed to get access token", "details": response.text}), response.status_code
        except Exception as e:
            app.logger.error(f"Error: {e}")  # Log any exceptions
            return jsonify({"error": "Request to API failed"}), 500
    else:
        return jsonify({"error": "No code provided"}), 400

# For Vercel to recognize the app
app = app