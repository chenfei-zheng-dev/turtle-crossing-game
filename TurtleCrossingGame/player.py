from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.home_position()
        self.finish_line = FINISH_LINE_Y

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)

    def home_position(self):
        self.goto(STARTING_POSITION)

