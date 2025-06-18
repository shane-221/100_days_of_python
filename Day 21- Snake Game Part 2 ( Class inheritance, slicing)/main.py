from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
# Todo: Initial prep of the code environment
screen= Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Stops the automatic movement


# Todo : Building of the snake body
snake = Snake()
food = Food()
score= Scoreboard()


# Todo : Application of the Keystroke
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Todo: Getting the snake to move
game_is_on=True
while game_is_on:
    screen.update()        # Updating the movement of the snake with a timeout to see.
    time.sleep(0.1)

    snake.move()
    # Todo: Detect whether the food and the snake collide.
    if snake.head.distance(food)< 15:
        food.refresh()
        score.increase_score()















# Todo: Exit screen.
screen.exitonclick()