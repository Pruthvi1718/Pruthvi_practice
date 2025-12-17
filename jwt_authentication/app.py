from flask import Flask, render_template, request, redirect, url_for
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Dummy database
users = {}

app = Flask(__name__)

# Dummy user storage
users = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

# REGISTER
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users[username] = password
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return f"<h2>Welcome {username}! Login Successful</h2>"
        else:
            return "<h2>Invalid Credentials</h2>"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
