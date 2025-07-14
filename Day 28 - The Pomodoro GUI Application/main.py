from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- UI SETUP ------------------------------- #

# Todo: Building of the screen
window =Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg =YELLOW)

# Todo: Placing the image on the screen.
canvas  = Canvas(width =200, height=224 ,  highlightthickness=0)
canvas.config(bg= YELLOW)
tomato_img = PhotoImage(file="tomato.png")          # Image will not learn the tomato file. Hence, need to
                                                    ## read through the file and get access to the location.
canvas.create_image(100, 112, image =tomato_img)
canvas.create_text(100, 130, text ="00:00", fill= "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column = 1)
                                        # Need to create padding on each side of the picture to make it look cleaner

# Todo: placing the title on the screen
total_label = Label(text="Study Timer", font =( " Arial", 30, "normal"), fg= GREEN, bg= YELLOW)
total_label.grid(column= 1, row =  0)

# ---------------------------- TIMER RESET ------------------------------- #
timer_reset = Button(text ="Reset",  highlightthickness= 0)
timer_reset.grid(row = 2, column =3)

# ---------------------------- TIMER MECHANISM ------------------------------- #
# Todo: Timer Button
timer_start = Button(text= "Start", highlightthickness= 0)
timer_start.grid(row = 2, column = 0)

# Todo: Timer tick mark
#Text
check_marks = Text(height=5, width=30)
check_marks  = Label(text="✓", font =( " Arial", 20, "normal"), fg= GREEN, bg= YELLOW)
check_marks.grid(column= 1, row =  3)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #



window.mainloop()