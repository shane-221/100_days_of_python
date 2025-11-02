from flask import Flask, render_template
import random
from datetime import date




app = Flask(__name__)

@app.route("/")
def home():
    now = date.today().year
    random_number = random.randint(1,10)
    return render_template("index.html", num = random_number, years= now)

if __name__ == "__main__":
    app.run(debug= True)