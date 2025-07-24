from tkinter import *
import pandas as pd
import random
#----------------------------------------------------- Constants-------------------------------------------------------#
FONT_HEADING = ( " Arial", 18, "bold")
FONT_GENERAL= ( " Arial", 22, "italic")
BACKGROUND_COLOUR= "#B1DDC6"

#---------------------------------------------------Use of the French Words--------------------------------------------#
# Todo: Opening the dataset
dataset= pd.read_csv("./data/french_words.csv")
# Todo: Turning them into key value pairs with each row
dataset = dataset.to_dict(orient= "records")

#---------------------------------------------------Functionalities----------------------------------------------------#
# Todo:  French word changes anytime the button is clicked
current_word ={}
def next_foreign_word():
    global current_word
    current_word= random.choice(dataset)
    french_word = current_word["French"]

    canvas.itemconfig(word_text, text = french_word)
    canvas.itemconfig(canvas_image, image= front_logo)
    canvas.itemconfig(title_word, text = " French")

# Todo: Flipping the card over + English title + Corresponding english word.
def english_word():
    # Todo: Canvas Change to Green
    canvas.itemconfig(canvas_image, image=back_logo)
    # Todo changing the title word
    canvas.itemconfig(title_word, text =" English")
    # Todo: Changing the french to the english
    canvas.itemconfig(word_text, text =current_word["English"])
    global timer
    timer = window.after(3000, start_loop)


#--------------------------------------------------------- Highest order Functions-------------------------------------#
timer= None
def start_loop():
    next_foreign_word()
    # Todo: Without clicking timer starts
    global timer
    timer = window.after(3000, english_word)

    # Todo : added the timer cancel through the buttons + If it cancels start back at this loop.


# Todo: cancel the timer if they click it:
def cancel_timer():
    # Todo: Clicking resets the timer
    window.after_cancel( timer)
    # Todo: Goes back to the start loop for the french
    start_loop()




#----------------------------------------Opening interface stuff-------------------------------------------------------#
                ########################--- Building the Screen---########################
# Todo: window function
window = Tk()
window.title("Flashcard App" )
window.config(padx=20, pady= 20, bg=BACKGROUND_COLOUR)
                ########################---Photo images---#################################
back_logo = PhotoImage(file ="./images/card_back.png")
front_logo= PhotoImage(file ="./images/card_front.png")



# Todo: Canvas to create the front card first creation
canvas = Canvas (width= 800, height  = 526)

canvas_image = canvas.create_image(400, 263, image = front_logo)
canvas.config(bg = BACKGROUND_COLOUR, highlightthickness=0)
canvas.grid(row=0, column =0,columnspan= 2)

                    ####################--- Words on the Canvas---########################
# Todo: Adding the language text onto the canvas first creation

title_word = canvas.create_text( 400,  200,text = "French ", font= FONT_GENERAL)
word_text = canvas.create_text( 400, 300, text = f"" , font= FONT_HEADING)



                    ####################---Buttons on the Screen---######################
# Todo: Canvas to create the right card

right_logo= PhotoImage(file = "./images/right.png")
right_button  = Button(image= right_logo, bg=BACKGROUND_COLOUR, command = cancel_timer)
right_button.grid(row=1, column =1)

# Todo: Canvas to create the wrong card

wrong_logo= PhotoImage(file ="./images/wrong.png")
wrong_button  = Button(image= wrong_logo, bg=BACKGROUND_COLOUR, command= cancel_timer)
wrong_button.grid(row=1, column =0)

#--------------------------------------------- Running the system as a loop------------------------------------------#
start_loop()


#-----------------------------------------------------Exit when needed-------------------------------------------------#
window.mainloop()