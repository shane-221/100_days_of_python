from flask  import Flask

app = Flask("website")


@app.route("/")
def home():
    return print("Welcome to my homepage")


