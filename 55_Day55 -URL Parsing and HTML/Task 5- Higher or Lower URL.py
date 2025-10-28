from flask import Flask
import random
app = Flask(__name__)

START_NUMBER=0
FINISH_NUMBER=9

# Todo:---------------------------------------Homepage-----------------------------------------------------------------#
def page_1(func):
    def wrapper_function():
        return """
            <h1>Guess a number between 0 and 9</h1>
            <iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" style="" frameBorder="0" 
            class="giphy-embed" allowFullScreen></iframe>
            <p><a href="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC">via GIPHY</a></p>"""
    return wrapper_function


#Todo:-------------------------------------------Random Number---------------------------------------------------------#
random_number= random.randint(START_NUMBER,FINISH_NUMBER)

#tODO:------------------------------------Functionalities--------------------------------------------------------------#

@app.route("/")
def greet():
        return "<h1>Guess a number between 0 and 9</h1>"  \
                "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__=="__main__":
    app.run(debug= True)