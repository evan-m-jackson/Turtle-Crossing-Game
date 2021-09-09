
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
import time

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, random.randrange(-250, 250, MOVE_INCREMENT))
        self.shapesize(stretch_len=2)
        self.movement = STARTING_MOVE_DISTANCE
        self.speed_time = 0.1
        self.move()

    def add_car(self):
        new_car = CarManager()
        self.car_list.append(new_car)

    def move(self):
        new_x = self.xcor() - self.movement
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        self.speed_time *= 0.75



