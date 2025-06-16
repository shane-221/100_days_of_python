from turtle import Screen, Turtle
import time
# Todo: Initial prep of the code environment
screen= Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #


# Todo : Building of the snake body

x=0
y=0
snake_positions=[]
for i in range(0,3):
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.penup()
    snake.goto(x,y)
    snake_positions.append(snake)
    x-=20
    y-=0

# Todo: Getting the snake to move
game_is_on=True
while game_is_on:

    for i in range(len(snake_positions)-1, 0, -1):
            # these code basically move all the snakes other than the first to the earlier ones location
        new_x=snake_positions[i-1].xcor()
        new_y= snake_positions[i-1].ycor()
        snake_positions[i].goto(new_x, new_y)
            # the first snakes location neds to be adjusted as well.
    snake_positions[0].forward(20)















# Todo: Exit screen.
screen.exitonclick()