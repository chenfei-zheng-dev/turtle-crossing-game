import turtle
from turtle import Turtle
turtle.colormode(255)


class Light(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(105, 105, 105)
        self.penup()
        self.shapesize(stretch_wid=6, stretch_len=6)

