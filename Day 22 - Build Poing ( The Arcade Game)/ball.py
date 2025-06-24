from  turtle import Turtle
import random

RIGHT_LIST=list(range(0,80))

class Ball(Turtle):

    def __init__(self):                 # Todo: Changes everything into turtle class
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
                                    # Todo: Turtle to move while accounting for the vertical boundaries
    def move(self):
        if self.ycor() >= 280:          # sTART WITH THE SPECIFIC CASES THEN MOVE DOEN TO THE GENERAL ONES
            angle= random.randint(280, 350)
            self.setheading(angle)      # Can also run another method. Where we increase or decrease by 10.
            self.forward(30)            ## But there is a lack of dynamism for the angle. Hence, I  used my
                                        ### own method.
        elif self.ycor()<=-280:
            angle= random.randint(0, 90)
            self.setheading(angle)
            self.forward(30)

        elif -280 < self.ycor() < 280:
            self.forward(30)


                                    # Todo: setting of the initial direction. Need to pull a random angle though
    def direction(self):
        angle =290
        self.setheading(angle)


                                    # Todo: Detect collisions relative to the side of the paddle
                                    ## Need to define the angles of rebound separately. Relative to where the paddle is
    def detect_collision(self, paddle_list, main_length_angle, upper_width_angle, lower_width_angle):
        for item in paddle_list:
                    # Looping through each of the square from the paddle. Finding the leftmost coordinate. Then pushing
                    ## the ball back
            left_side = (item.xcor()-10, item.ycor())
            upper_side= (item.xcor(), item.ycor()+10)
            lower_side =(item.xcor(), item.ycor()-10)
                    # Left side of the paddle
            if self.distance(left_side)<10:
                angle = random.randint(*main_length_angle)
                self.setheading(angle)
                self.forward(30)
                break
                    # Upper side of the paddle
            elif self.distance(upper_side)<10:
                angle = random.randint(*upper_width_angle)
                self.setheading(angle)
                self.forward(30)
                break                   # Good idea to exit the loop given that only one point would be reached
                    # Lower side of the paddle
            elif self.distance(lower_side) < 10:
                angle = random.randint(*lower_width_angle)
                self.setheading(angle)
                self.forward(30)
                break

























