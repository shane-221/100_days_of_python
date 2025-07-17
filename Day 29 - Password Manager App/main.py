from tkinter import *
FONT = ( " Arial", 12, "bold")

#--------------------------------------Building the Screen ------------------------------------------------------------#


        #####################----- Building the image section -----################

# Todo: window functions
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# Todo: Canvas with the image
canvas = Canvas( width = 200,height= 200, highlightthickness= 0)
logo_ing =PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image= logo_ing )
canvas.grid(row= 0,column =1)

        #####################-----Button Sections-----###########################
# Todo: Add button
add_button = Button(text= "Add ", command  = None, width = 36)
add_button.grid(row=4, column= 1, columnspan= 2, sticky= "ew")

# Todo: Generate Password Button
password_button= Button(text =" Generate Password" , command  = None, width=15, padx= 30)
password_button.grid(row= 3, column= 2)


        #####################-----Entry Section-----##############################
# Todo: Password write section
password_input = Entry( width = 36)
password_input. grid(row= 3, column = 1, sticky= "ew")

# Todo: Email section
email_input = Entry( width =36)
email_input. grid(row= 2, column = 1, columnspan = 2, sticky="ew")

# Todo: Website section
website_input = Entry( width =36 )
website_input. grid(row= 1, column = 1, columnspan= 2, sticky= "ew")



        ####################----- Text Section-----###############################
# Todo: Password Label
password_text = Label(text ="Password:", font=FONT )
password_text.grid( row= 3, column = 0)

# Todo:  Email/ Username Label
password_text = Label(text ="Email/ Username:", font=FONT )
password_text.grid( row= 2, column = 0)

# Todo:  Website Label
password_text = Label(text ="Website:", font=FONT )
password_text.grid( row= 1, column = 0)



#----------------------------------------------Exit when needed--------------------------------------------------------#
mainloop()