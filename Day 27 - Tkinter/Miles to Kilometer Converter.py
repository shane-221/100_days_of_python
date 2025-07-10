from tkinter import *



# Todo: Opening the window. But need to Keep the window open.
window =Tk()

    # Todo: changing the title of the program:
window.title("Miles to Km Converter")
    # Todo: adjust the size of the screen.
window.minsize(width=300, height = 100)



# Todo: Creating the button to Click:
button  = Button( text= "Calculate", )
button.grid(column=1, row=2)



# Todo: Creating all the text
    # Todo: KM Label
my_label = Label(text="KM", font =( " Arial", 10, "normal"))
my_label.grid(column= 2, row =  1)

    # Todo; Creating the changing Km Function
km =0
my_label = Label(text=f"{km}", font =( " Arial", 10, "normal"))
my_label.grid(column= 1, row =  1)
    # Todo: is equal to part
my_label = Label(text="is equal to", font =( " Arial", 10, "normal"))
my_label.grid(column= 0, row =  1)

    # Todo: Miles letters
my_label = Label(text="Miles", font =( " Arial", 10, "normal"))
my_label.grid(column= 3, row =  0)


# Todo: Entry or Text Boxes
input  = Entry(width=20)
input.grid(column=1, row=0)




# Todo: Keeps the window running
window.mainloop()