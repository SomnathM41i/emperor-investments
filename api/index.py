from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Emperor Investments!"

@app.route("/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    if code:
        return jsonify({"message": "Authorization code received", "code": code})
    else:
        return jsonify({"error": "No code provided"}), 400

# For Vercel to recognize the app
app = app
