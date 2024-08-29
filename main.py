import time
from turtle import Screen
import car_manager
from player import Player
from car_manager import CarManagerClass
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManagerClass()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create()
    car_manager.move()

    #Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful travel
    if player.finish_line():
        player.start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()