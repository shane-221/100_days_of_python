#Objective: Create a new server with Flask
from flask import Flask


app = Flask(__name__)

# Setting upp the webserver
@app.route("/bye")                                                                                                      # The decorator says if they access the website/ bye, then apply the def function below
def say_bye():                                                                                                          # Can check if you put /bye on the url 
    return "<p>Bye!</p>"

if __name__ == "__main__":
    app.run()