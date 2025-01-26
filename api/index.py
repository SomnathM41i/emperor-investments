from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Emperor Investments!"

@app.route("/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    if code:
        # Exchange the authorization code for an access token
        response = requests.post(
            "https://api.smartapi.angelbroking.com/oauth2/token",
            data={
                "client_id": "vd46TdQP",
                "client_secret": "4ddeaa34-c192-4154-85e1-9211266bd663",
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": "https://emperor-investments.vercel.app/callback"
            }
        )
        if response.status_code == 200:
            return response.json()  # Return the access token or other data
        else:
            return jsonify({"error": "Failed to get access token"}), response.status_code
    else:
        return jsonify({"error": "No code provided"}), 400

# For Vercel to recognize the app
app = app
