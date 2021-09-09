STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(STARTING_POSITION)
        self.goalpost = FINISH_LINE_Y

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def finished(self):
        self.goto(STARTING_POSITION)

