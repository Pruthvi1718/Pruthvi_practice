from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def first():
    return "<h1> HELLO FLASK! </h1>"

app.run()