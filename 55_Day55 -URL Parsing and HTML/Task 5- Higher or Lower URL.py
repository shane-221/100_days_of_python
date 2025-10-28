from flask import Flask
app = Flask(__name__)

def page_1(func):
    def wrapper_function():
        return """
                <h1>Welcome to my homepage</h1>
                <iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
                <p><a href="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC">via GIPHY</a></p>"""
    return wrapper_function





@app.route("/")
@page_1
def greet():
        None


if __name__=="__main__":
    app.run(debug= True)