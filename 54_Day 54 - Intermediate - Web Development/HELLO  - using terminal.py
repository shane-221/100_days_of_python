#Objective: Create a new server with Flask
from flask import Flask


app = Flask(__name__)

# Setting upp the webserver
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Can use the Termianl to run the Flask app server or use the code below:@

if __name__ == "__main__":
    app.run()
                                                                                                                        # Name is the same as __main__ therefore this code makes it run as a script


