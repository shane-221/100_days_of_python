from flask  import Flask

app = Flask("website")


@app.route("/")
def home():
    return "Welcome to my homepage"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}. Welcome to my homepage"


@app.route("/username/<names>/<number>")
def greeting(names, number):
    return f"""
                Hello {names}. Welcome to my homepage
                Hello {number}. Welcome to my homepage
            """

if __name__=="__main__":
    app.run(debug= True)


