from flask import Flask, render_template
import requests




app = Flask(__name__)

@app.route("/guess/<name>")
def home(name):
    gender = requests.get(f"https://api.genderize.io?name={name}")
    age = requests.get(f"https://api.agify.io?name={name}")

    gender = gender.json()["gender"]
    age =age.json()["age"]
    return render_template("index.html", names=name.title(), ages=age, genders =gender)

if __name__ == "__main__":
    app.run(debug= True)