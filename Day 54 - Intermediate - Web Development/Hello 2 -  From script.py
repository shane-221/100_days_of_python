#Objective: Create a new server with Flask
from flask import Flask


app = Flask(__name__)

# Setting upp the webserver
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


