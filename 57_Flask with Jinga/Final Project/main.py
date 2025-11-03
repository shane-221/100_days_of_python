import json

from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def cactus():
    with open("../Final Project/static/blog-data.txt", mode="r") as words:
        text = words.read()
        blog_data =json.loads(text)
    return render_template("index.html", blog= blog_data)

if __name__ == "__main__":
    app.run(debug=True)
