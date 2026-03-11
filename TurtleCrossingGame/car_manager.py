from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
DARK_COLORS = [(0, 0, 0,), (56, 56, 56), (128, 128, 128), (200, 200, 200)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self, mode):
        super().__init__()
        # For the car_manager Object itself to be invisible
        self.hideturtle()

        self.dark_colors = DARK_COLORS
        self.mode = mode
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []
        self.level = 1
        self.max_rand_num = 6
        self.add_new_car()

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def add_new_car(self):
        rand_num = random.randint(1, self.max_rand_num)
        if rand_num == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            if self.mode != "hard":
                new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            rand_y = random.randint(-250, 250)
            new_car.goto(y=rand_y, x=320)
            self.cars.append(new_car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
        if self.level % 2 == 0:
            if self.max_rand_num != 2:
                self.max_rand_num -= 1

        self.level += 1
