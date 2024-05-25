import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)
screen.listen()

turtles = []
is_game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_game_on:
    # update the screen with whatever action that was taken
    # after 1-second delay so that the snake looks as it is
    # one piece instead of three squares following one another
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 25:
        scoreboard.increase()
        food.refresh()
        snake.grow()
    is_game_on = snake.check_collide_with_boarders()
    if not is_game_on:
        scoreboard.display_game_over()
    else:
        is_game_on = snake.check_collide_with_body()
        if not is_game_on:
            scoreboard.display_game_over()

screen.exitonclick()
