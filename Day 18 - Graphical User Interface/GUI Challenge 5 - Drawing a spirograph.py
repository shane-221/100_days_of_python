import turtle
from turtle import Screen
import turtle as t
import random

turtle.colormode(255)
timmy=t.Turtle()
timmy.speed(10)
timmy.pensize(5)

def random_colour():
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)
    colour_scheme = (x, y, z)
    return colour_scheme

for i in range(0, 36):
    timmy.pencolor(random_colour())
    timmy.circle(100)
    timmy.right(10)

# Todo 3:  Exit on click function
my_screen = Screen()
my_screen.setup (width=150, height=150, startx=0, starty=0)
my_screen.exitonclick()
