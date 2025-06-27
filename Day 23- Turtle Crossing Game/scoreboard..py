from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-260, 260)
        self.write(self.score,*FONT)

