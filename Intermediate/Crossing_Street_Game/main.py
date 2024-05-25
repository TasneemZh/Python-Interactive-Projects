import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

screen.listen()
screen.onkey(player.cross_a_street, "Up")

game_is_on = True
wait_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if wait_counter > 6:
        car_manager.create_random_car()
        wait_counter = 0
    car_manager.move()
    wait_counter += 1
    game_is_on = car_manager.check_collision(player)
    if not game_is_on:
        scoreboard.display_game_over()
    else:
        if player.reached_the_end():
            scoreboard.level_up()
            car_manager.speed_up()
