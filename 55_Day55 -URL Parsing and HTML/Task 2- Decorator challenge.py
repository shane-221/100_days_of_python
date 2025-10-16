from flask import Flask
app = Flask(__name__)


def bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function
def underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function
def italics(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


@app.route("/")
@bold
@underline
@italics
def home():
    return " Welcome to my Homepage"


if __name__=="__main__":
    app.run(debug= True)



# @app.rote("/final")
# def end():
#     return "Goodbye"

