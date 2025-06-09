from turtle import Turtle, Screen

#Todo 1: The instance of Timmy the Turtle being created.

timmy_the_turtle= Turtle()
    # Changing the shape of the turtle
timmy_the_turtle.shape("turtle")
    # Changing the colour of the turtle:
timmy_the_turtle.color("red")

# Todo 2: Turtle challenges
    # Todo 2.A Create a square:
for i in range(1,5):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


# Exit on click function
my_screen = Screen()
my_screen.exitonclick()

