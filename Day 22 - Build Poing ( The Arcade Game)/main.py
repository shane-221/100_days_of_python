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


# Todo: Creating two boards from the Paddle class
R_PADDLE=(310,50)
L_PADDLE=(-310,50)

r_board= Paddle()
r_board.create_board(side = R_PADDLE)
l_board= Paddle()
l_board.create_board(side=L_PADDLE)

# Todo: Being able to move the paddle
            # For right paddle
screen.listen()
screen.onkey(r_board.up, "Up")
screen.onkey(r_board.down, "Down")

            # For left Paddle
screen.listen()
screen.onkey(l_board.up, "w")
screen.onkey(l_board.down, "s")

# Todo : Need to update from the changes since the tracer is off.
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.02)






















screen.exitonclick()