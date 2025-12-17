from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Dummy user storage
users = {}

@app.route("/")
def home():
    return redirect(url_for("login"))


#SIGNUP
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users[username] = password
        return redirect(url_for("login"))

    return render_template("signup.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            access_token = create_access_token(identity=username)
            return render_template("dashboard.html", token=access_token)

        return "Invalid credentials"

    return render_template("login.html")

#PROTECTED API
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f"Hello {current_user}, this is a protected route")

if __name__ == "__main__":
    app.run(debug=True)
