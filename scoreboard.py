FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        t = Turtle()
        t.hideturtle()
        t.write("GAME OVER", align="center", font=FONT)

    def add_score(self):
        self.level += 1
        self.update_scoreboard()