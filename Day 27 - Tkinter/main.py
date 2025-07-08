import tkinter

# Todo: Opening the window. But need to Keep the window open.
window =tkinter.Tk()

    # Todo: changing the title of the program:
window.title("My first GUI Program")
    # Todo: adjust the size of the screen.
window.minsize(width=500, height = 300)

# Todo: Adding Labels as a class( need to say how it will could be layed out)
my_label = tkinter.Label(text="I am a Label", font =( " Arial", 24, "bold"))
    # Todo: Laying out how the lable will be laid out on the screen:
my_label.pack()

# Todo: Keeps the window running
window.mainloop()
