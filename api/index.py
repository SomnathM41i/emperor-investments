from flask import Flask, request, jsonify
import requests

# Initialize the Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Emperor Investments!"

@app.route("/callback", methods=["GET"])
def callback():
    # Get the authorization code from the URL
    code = request.args.get("code")
    
    if code:
        # Prepare the request data for exchanging the code for an access token
        data = {
            "client_id": "vd46TdQP",  # Your client ID
            "client_secret": "4ddeaa34-c192-4154-85e1-9211266bd663",  # Your client secret
            "code": code,  # The authorization code from the URL
            "grant_type": "authorization_code",  # Grant type is authorization code
            "redirect_uri": "https://emperor-investments.vercel.app/callback"  # The same redirect URI used in the OAuth process
        }

        # Make a POST request to exchange the code for an access token
        response = requests.post("https://api.smartapi.angelbroking.com/oauth2/token", data=data)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # Return the access token or the entire response (can also store the token for future use)
            return jsonify(response.json())  # Return JSON containing the access token and other info
        else:
            # If the token request failed, return an error message
            return jsonify({"error": "Failed to get access token"}), response.status_code
    else:
        # If no 'code' is found in the request, return an error message
        return jsonify({"error": "No code provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
