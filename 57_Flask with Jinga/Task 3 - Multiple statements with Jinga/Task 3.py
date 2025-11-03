import json

from flask import Flask, render_template
import requests




app = Flask(__name__)

@app.route("/guess/<name>")
def home(name):
    gender = requests.get(f"https://api.genderize.io?name={name}")
    age = requests.get(f"https://api.agify.io?name={name}")

    gender = gender.json()["gender"]
    age =age.json()["age"]
    return render_template("blog.html", names=name.title(), ages=age, genders =gender)

@app.route("/blog")
def blog():
    with open("static/blog-data.txt", mode="r") as words:
        text = words.read()
        blog_data =json.loads(text)
    return render_template("blog.html", blog= blog_data)

if __name__ == "__main__":
    app.run(debug= True)