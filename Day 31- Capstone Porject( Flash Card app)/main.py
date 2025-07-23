from tkinter import *

#----------------------------------------------------- Constants-------------------------------------------------------#
FONT_HEADING = ( " Arial", 18, "bold")
FONT_GENERAL= ( " Arial", 22, "italic")
BACKGROUND_COLOUR= "#00FF7F"
#-----------------------------------------------------UI Interface-----------------------------------------------------#
                ########################--- Building the Screen---########################
# Todo: Window function
window = Tk()
window.title("Flashcard App" )
window.config(padx=20, pady= 20, bg=BACKGROUND_COLOUR)

# Todo: Canvas to create the front card
canvas = Canvas (width= 400, height  = 300)
front_logo= PhotoImage(file ="./images/card_front.png")
canvas.create_image(200, 150, image = front_logo)
canvas.grid(row=0, column =0, pady= 50, padx= 50, columnspan= 2)

                    ####################---Buttons on the Screen---######################
# Todo: Canvas to create the right card
canvas1 = Canvas (width=  100, height  = 100)
right_logo= PhotoImage(file = "./images/right.png")
canvas1.create_image(50, 50, image = right_logo)
canvas1.grid(row=1, column =1, pady= 2, padx= 2)

# Todo: Canvas to create the wrong card
canvas2 = Canvas (width= 100, height  = 100)
wrong_logo= PhotoImage(file ="./images/wrong.png")
canvas2.create_image(50, 50, image = wrong_logo)
canvas2.grid(row=1, column =0, pady= 2, padx= 2)
                    ####################---Words on the Canvas---########################
#Todo: Adding the foreign language text onto the canvas

canvas.create_text( 200,  100,text = "French ", font= FONT_GENERAL)
canvas.create_text( 200, 200, text = "French Word ", font= FONT_HEADING)



#-----------------------------------------------------Exit when needed-------------------------------------------------#
window.mainloop()