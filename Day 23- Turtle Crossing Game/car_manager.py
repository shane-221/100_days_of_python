from turtle import Turtle

# Todo: Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):
        # Todo: Improt all the classes from the modules and Variables that are used.
    def __init__(self):
        super().__init__()
        self.one_car = []
        self.start_coordinates = (320, -260)
        self.create_one_car()


        # Todo: creating one car with 2 squares and placing them into a list
    def create_one_car(self):
        for i in range(0,2):
            i= Turtle()
            i.shape("square")
            self.hideturtle()
            self.penup()
            i.goto(self.start_coordinates)
            self.one_car.append(i)
            x_cor = self.start_coordinates[0]+20
            y_cor =self.start_coordinates[1]
            self.start_coordinates = (x_cor, y_cor)
        # Todo: moving each within the one car list  by 5 units.
    def move_one_car(self):
        for i in self.one_car:
            self.penup()
            x_cor =i.xcor()
            y_cor =i.ycor()
            i.goto(x_cor-5, y_cor)
