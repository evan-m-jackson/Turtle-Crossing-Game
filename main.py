import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

p = Player()

screen.onkey(p.move_forward, "Up")

car = CarManager()
car_list = [car]
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(car.speed_time)
    screen.update()
    for c in car_list:
        c.move()
        if c.xcor() == 260:
            new_car = CarManager()
            car_list.append(new_car)
        if p.distance(c) < 25:
            score.game_over()
            game_is_on = False
        if p.ycor() == p.goalpost:
            p.finished()
            score.add_score()
            car.increase_speed()




screen.exitonclick()