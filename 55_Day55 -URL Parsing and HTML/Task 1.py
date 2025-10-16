from flask  import Flask

app = Flask("website")


@app.route("/")
def home():
    return "Welcome to my homepage"


# Todo: adding dynamic variables
@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}. Welcome to my homepage"

# Todo: addding multiple dynamic variables
@app.route("/username/<names>/<number>")
def greeting(names, number):
    return f"""
                Hello {names}. Welcome to my homepage
                Hello {number}. Welcome to my homepage
            """
# Todo: Can also add html code into it
@app.route("/bye")
def bye():
    return '<h1> "Bye"</h1>'\
            '<img scr ="......." width =200> '


if __name__=="__main__":
    app.run(debug= True)


