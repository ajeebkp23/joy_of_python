from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/<username>')
def profile(username):
    return f'Welcome to {username}\'s profile'
