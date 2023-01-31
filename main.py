import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create Turtle player
turtle_player = Player()

# Create scoreboard
scoreboard = Scoreboard()

# Create car
car_manager = CarManager()

# Control the turtle
screen.onkey(key="Up", fun=turtle_player.move_forward)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars and move them
    car_manager.create_car()
    car_manager.move_cars()

    # Detect touching to the top to move to next level
    if turtle_player.ycor() >= 290:
        scoreboard.next_level()
        turtle_player.reset_turtle()

    # Detect if hit by car
    for car in car_manager.cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()