from  turtle import Turtle, Screen
import random

RIGHT_LIST=list(range(0,80))

class Ball(Turtle):

    def __init__(self):                 # Changes everything into turtle class
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        if self.ycor() >= 280:          # sTART WITH THE SPECIFIC CASES THEN MOVE DOEN TO THE GENERAL ONES
            angle= random.randint(280, 350)
            self.setheading(angle)      # Can also run another method. Where we increase or decrease by 10.
            self.forward(20)            # But there is a lack of dynamism for the angle. Hence I have used my
                                        # own method.
        elif self.ycor()<=-280:
            angle= random.randint(0, 90)
            self.setheading(angle)
            self.forward(20)

        elif -280 < self.ycor() < 280:
            self.forward(20)



    def direction(self):
        angle = random.randint()
        self.setheading(angle)


























