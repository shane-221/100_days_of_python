from tkinter import *

#--------------------------------------Building the Screen ------------------------------------------------------------#
# Todo: window functions
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# Todo: create the canvas with the image
canvas = Canvas( width = 300,height= 300, highlightthickness= 0)
logo_ing =PhotoImage(file = "logo.png")
canvas.create_image(150, 100, image= logo_ing )
canvas.grid(row= 0,column =0)





#----------------------------------------------Exit when needed--------------------------------------------------------#
mainloop()