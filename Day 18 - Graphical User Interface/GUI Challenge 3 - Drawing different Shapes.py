from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
import random
import turtle

# Colour scheme to be moved from the standard 0 to 1 to o to 255
turtle.colormode(255)


# Todo 1: Turtle challenges
total_angle = 360
number_of_sides = 3

while number_of_sides<11:
    actual_angle = total_angle / number_of_sides
    
    for i in range(0,number_of_sides):
        x = random.randint(0, 255)
        y = random.randint(0, 255)
        z = random.randint(0, 255)
        timmy_the_turtle.pencolor(x,y,z)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(actual_angle)
    number_of_sides+=1

# Exit on click function
my_screen = Screen()
my_screen.exitonclick()