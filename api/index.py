from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Emperor Investments!"

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Validate login (this is just an example; you should hash passwords and check a database)
    if email == "test@example.com" and password == "password123":
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

@app.route("/dashboard")
def dashboard():
    return "Welcome to the Dashboard!"

if __name__ == "__main__":
    app.run(debug=True)
