import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



# Initializing player, cars and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listening for commands
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increment_level()
        scoreboard.write_level()

scoreboard.game_over()

screen.exitonclick()


