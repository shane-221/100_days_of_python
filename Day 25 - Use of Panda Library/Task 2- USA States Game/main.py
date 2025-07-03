import turtle

# Todo: Creation of the Screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Todo: Loading Turtle as an image
image = "blank_states_img.gif"
        # Shape can be any image file
screen.addshape(image)
        # Need to then be used by a turtle
turtle.shape(image)






























screen.exitonclick()