from tkinter import *
import pandas as pd
#----------------------------------------------------- Constants-------------------------------------------------------#
FONT_HEADING = ( " Arial", 18, "bold")
FONT_GENERAL= ( " Arial", 22, "italic")
BACKGROUND_COLOUR= "#B1DDC6"

#---------------------------------------------------Functionality of the Button ---------------------------------------#
# Todo: Opening the dataset
dataset= pd.read_csv("./data/french_words.csv")
# Todo: Turning them into key value pairs with each row
dataset = dataset.to_dict(orient= "records")
# Todo: Matching them into french: english pairs and a list of pure french words
combined_data = { item["French"]: item["English"] for item in dataset }
list_of_french = [ item for item in combined_data]

# Todo: word changes anytime the button is clicked
n=0
def next_foreign_word():
    word = list_of_french[n]
    n+1



#-----------------------------------------------------UI Interface-----------------------------------------------------#
                ########################--- Building the Screen---########################
# Todo: Window function
window = Tk()
window.title("Flashcard App" )
window.config(padx=20, pady= 20, bg=BACKGROUND_COLOUR)

# Todo: Canvas to create the front card
canvas = Canvas (width= 800, height  = 526)
front_logo= PhotoImage(file ="./images/card_front.png")
canvas.create_image(400, 263, image = front_logo)
canvas.config(bg = BACKGROUND_COLOUR, highlightthickness=0)
canvas.grid(row=0, column =0,columnspan= 2)

                    ####################---Words on the Canvas---########################
# Todo: Adding the foreign language text onto the canvas

canvas.create_text( 400,  200,text = "French ", font= FONT_GENERAL)
canvas.create_text( 400, 300, text = "French Word ", font= FONT_HEADING)


                    ####################---Buttons on the Screen---######################
# Todo: Canvas to create the right card

right_logo= PhotoImage(file = "./images/right.png")
right_button  = Button(image= right_logo, bg=BACKGROUND_COLOUR)
right_button.grid(row=1, column =1)

# Todo: Canvas to create the wrong card

wrong_logo= PhotoImage(file ="./images/wrong.png")
wrong_button  = Button(image= wrong_logo, bg=BACKGROUND_COLOUR)
wrong_button.grid(row=1, column =0)


#-----------------------------------------------------Exit when needed-------------------------------------------------#
window.mainloop()