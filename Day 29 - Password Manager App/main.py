from tkinter import *
import pandas as pd

#---------------------------------------------Constants----------------------------------------------------------------#
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


# ----------------------------------------------Functionalities---------------------------------------------------------#
# Todo: Saving the data. Creating an embedded list, then convert to data frame, then to a text file

        # Todo: Creating an embedded list
data_list =[]
def save():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()
    item_list =[website_value, email_value, password_value]
    data_list.append(item_list)
    dataset = pd.DataFrame(item_list)
    dataset.to_csv("Password record.csv", mode ="a")

            # Todo: convert that list into a data frame
def print_results():


#--------------------------------UI Interface -------------------------------------------------------------------------#

        #####################-----Button Sections-----###########################
# Todo: Add button
add_button = Button(text= "Add ", command  = save, width = 36)
add_button.grid(row=4, column= 1, columnspan= 2, sticky= "ew")

# Todo: Generate Password Button
password_button= Button(text =" Generate Password" , command  = print_results, width=15, padx= 30)
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
website_input.focus
website_input.insert(0, "Enter email")



        ####################----- Text Section-----###############################
# Todo: Password Label
password_text = Label(text ="Password:", font=FONT )
password_text.grid( row= 3, column = 0)

# Todo:  Email/ Username Label
email_text = Label(text ="Email/ Username:", font=FONT )
email_text.grid( row= 2, column = 0)

# Todo:  Website Label
website_text = Label(text ="Website:", font=FONT )
website_text.grid( row= 1, column = 0)
            # Allows you to pre-populate the file.




#----------------------------------------------Exit when needed--------------------------------------------------------#
mainloop()