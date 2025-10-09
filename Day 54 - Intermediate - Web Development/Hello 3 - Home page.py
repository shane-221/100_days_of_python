#Objective: Create a new server with Flask
from flask import Flask


app = Flask(__name__)

# Setting upp the webserver
@app.route("/")                                                                                                         # The first slash represents the homepage.
def hello_world():                                                                                                      ## I.e. when the user gets to the first page with the first slash show them the def function
    return "<p>Hello, World!</p>"                                                                                       ## "@" bit represents a python decorator. Offer additional functionalities to existing code.

                                                                                                                        # Functions are first class objects. Therefore, you can use them as arguments.

                                                                                                                        # you can create functions within functions as well. 
if __name__ == "__main__":
    app.run()
