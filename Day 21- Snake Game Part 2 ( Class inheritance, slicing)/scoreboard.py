from turtle import Turtle


class Scoreboard( Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score=0
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score:{self.score}", False,align="center", font=("Arial", 15, "normal") )

    def increase_score(self):
        self.score+=1
        self.track_score()

