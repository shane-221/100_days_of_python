import turtle
from turtle import Screen,Turtle
import time
from paddle import Paddle
# Todo: Creation of the screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# Todo: Creating the board from the Paddle class
board= Paddle()
board.create_board()

# Todo: Being able to move the paddle
screen.listen()
screen.onkey(board.up, "Up")
screen.onkey(board.down, "Down")


game_is_on = True
while game_is_on:

    # Todo : Need to update from the changes since the tracer is off.
    screen.update()
    time.sleep(0.02)






















screen.exitonclick()