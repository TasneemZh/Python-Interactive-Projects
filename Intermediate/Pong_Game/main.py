import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=700)
screen.bgcolor("black")
screen.title("Pong Game 🏓")

right_paddle = Paddle("right")
left_paddle = Paddle("left")

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_over = False

while not is_game_over:
    time.sleep(0.1)
    screen.update()
    ball.move()
    ball.handle_boarders_collision()
    if not ball.handle_paddles_collision(right_paddle):
        if not ball.handle_paddles_collision(left_paddle):
            is_game_over = ball.check_if_ball_escaped()
            if is_game_over:
                scoreboard.game_over_text()
        else:
            scoreboard.increase("left")
    else:
        scoreboard.increase("right")

screen.exitonclick()
