from turtle import Turtle


class Paddle:

    def __init__(self):
        self.start_position = (350, 0)
        self.board_list = []
    def create_board(self):
        # Todo: Create the paddle

        for i in range(0, 5):
            square = Turtle()
            square.penup()
            square.shape("square")
            square.color("white")
            square.goto(self.start_position)
            self.board_list.append(square)
            x_cor = self.start_position[0]
            y_cor = self.start_position[1] - 20
            self.start_position = (x_cor, y_cor)

    def up(self):
        if self.board_list[0].ycor()<290:
            for square in self.board_list:
                new_y = square.ycor()+20
                square.goto(square.xcor(),new_y)

    def down(self):
        if self.board_list[-1].ycor()>-280:       # making sure there are boundary conditions for the extent to go down.
            for square in self.board_list:
                new_y = square.ycor()-20
                square.goto(square.xcor(),new_y)