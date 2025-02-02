from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")  # Renders the login page

@app.route("/api/login", methods=["POST"])
def login():
    email = request.form.get("email")  # Get email from form data
    password = request.form.get("password")  # Get password from form data

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
