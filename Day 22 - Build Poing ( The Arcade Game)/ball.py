from  turtle import Turtle, Screen
import time
X_COR= 380
Y_COR = 280

class Ball(Turtle):

    def __init__(self):                 # Changes everything into turtle class
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        if -260 <self.xcor()<260 or -360<self.ycor()<360  :
            new_x= self.xcor() + 25
            new_y = self.ycor() + 25
            self.goto(new_x, new_y)























