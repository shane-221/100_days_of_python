from turtle import Turtle, Screen
import time 


# Todo: creating the screen function
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


# Todo: Screen update function
game_on= True
while game_on:
    time.sleep(0.1)
    screen.update()


# Todo: Exit on click function
screen.exitonclick()