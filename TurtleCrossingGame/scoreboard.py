from turtle import Turtle
FONT = ("Montserrat", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, mode):
        super().__init__()
        if mode == "hard":
            self.color("white")
            self.data_file = "dark_high_score.txt"
        else:
            self.data_file = "color_high_score.txt"

        with open(self.data_file) as data:
            self.high_score = int(data.read())

        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 210)
        self.level_up()

    def level_up(self):
        self.level += 1
        if self.level > self.high_score:
            self.high_score = self.level
            with open(self.data_file, mode="w") as data:
                data.write(str(self.high_score))
        self.clear()
        self.write(f"Level: {self.level}\nHigh Score: {self.high_score}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over.", align="center", font=FONT)
