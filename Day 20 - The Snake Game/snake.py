from turtle import Turtle

class Snake:

    def __init__(self):

        self.number_of_snakes = []
        self.create_snake( )            # Automatically runs the method of create the snake when the Class is created.

    def create_snake(self):
        x = 0
        y = 0

        for i in range(0, 3):
            snake = Turtle()
            snake.color("white")
            snake.shape("square")
            snake.penup()
            snake.goto(x, y)
            self.number_of_snakes.append(snake)
            x -= 20
            y -= 0

    def move(self):
        for i in range(len(self.number_of_snakes)-1, 0, -1):
                # these code basically move all the snakes other than the first to the earlier ones location
            new_x = self.number_of_snakes[i-1].xcor()
            new_y =self.number_of_snakes[i-1].ycor()
            self.number_of_snakes[i].goto(new_x, new_y)
                # the first snakes location neds to be adjusted as well.
        self.number_of_snakes[0].forward(20)

