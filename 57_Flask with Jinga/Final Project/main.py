import json

from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def home():
    with open("../Final Project/static/blog-data.txt", mode="r") as words:
        text = words.read()
        blog_data =json.loads(text)
    return render_template("index.html", blog= blog_data)

@app.route("/post/<num>")
def posting(num):
    with open("../Final Project/static/blog-data.txt", mode="r") as words:
        text = words.read()
        blog_data =json.loads(text)
        posting = [ blog for blog in blog_data if str(blog["id"])==str(num) ]
        print(posting)
    return render_template("post.html", post= posting[0])

if __name__ == "__main__":
    app.run(debug=True)
