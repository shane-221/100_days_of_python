from turtle import Turtle

class Snake:
    x = 0
    y = 0

    number_of_snakes = []
    for i in range(0, 3):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(x, y)
        number_of_snakes.append(snake)
        x -= 20
        y -= 0

    def move(self, snake_positions= number_of_snakes):
        for i in range(len(snake_positions)-1, 0, -1):
                # these code basically move all the snakes other than the first to the earlier ones location
            new_x = snake_positions[i-1].xcor()
            new_y = snake_positions[i-1].ycor()
            snake_positions[i].goto(new_x, new_y)
                # the first snakes location neds to be adjusted as well.
        snake_positions[0].forward(20)

