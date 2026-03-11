import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from light import Light

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("TurtleCrossing")

level_mode = turtle.textinput(title="Choose a difficulty", prompt="__Type 'easy' or 'hard':__").lower()

light = Light()
player = Player()
car_manager = CarManager(level_mode)
scoreboard = Scoreboard(level_mode)

if level_mode == "hard":
    screen.bgcolor("black")
    player.color("white")
else:
    light.hideturtle()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_new_car()
    car_manager.move()

    if level_mode == "hard":
        light.goto(player.position())
        for car in car_manager.cars:
            if car.distance(player) < 60:
                car.color(car_manager.dark_colors[3])
            elif car.distance(player) < 70:
                car.color(car_manager.dark_colors[2])
            elif car.distance(player) < 90:
                car.color(car_manager.dark_colors[1])
            else:
                car.color(car_manager.dark_colors[0])

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.ycor() == player.finish_line:
        player.home_position()
        car_manager.increase_speed()
        scoreboard.level_up()


screen.exitonclick()
