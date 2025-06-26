from turtle import Screen
from player import Player_Turtle
import time
from car_manager import Cars


# Todo: creating the screen function
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

# Todo: Addition of the Plater Turtle
player= Player_Turtle()

# Todo: Ability of the Player turtle to move
screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")

# Todo: Movement of the obstacles.
cars= Cars()
cars.car_manager()
cars.loop_the_cars()

# Todo: Screen update function
game_on= True

while game_on:
    time.sleep(0.1)
    screen.update()

    cars.move_one_car()



# Todo: Exit on click function
screen.exitonclick()