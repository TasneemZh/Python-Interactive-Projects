import random
from turtle import Turtle, Screen

WIDTH = 500
HEIGHT = 400
NUM_OF_TURTLES = 6

screen = Screen()
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
colors = ["red", "blue", "purple", "green", "yellow", "orange"]
turtles = []

user_bet = screen.textinput("Place Your Bet", "What is the color of the turtle that you think will win the race?")
if user_bet:
    race_on = True
else:
    race_on = False


def create_the_turtles():
    for i in range(NUM_OF_TURTLES):
        bob = Turtle()
        bob.shape("turtle")
        bob.color(colors[i])
        bob.penup()
        turtles.append(bob)


def position_the_turtles():
    y = 0
    i = 0
    sign = 1
    for turtle in turtles:
        if i == int(NUM_OF_TURTLES / 2):
            sign = -1
            y = 0
        else:
            y += (HEIGHT / 8) * sign
        i += 1
        turtle.goto(-1 * WIDTH / 2 - 30, y)


def run_turtles_race():
    for turtle in turtles:
        # x = turtle.xcor() + random.randint(1, 10)
        turtle.forward(random.randint(1, 10))
        print(turtle.xcor())
        if turtle.xcor() >= ((WIDTH/2) + 100):
            if user_bet == turtle.fillcolor():
                print(f"Congrats! The {turtle.fillcolor()} just won the race!")
            else:
                print(f"Unfortunately, the {turtle.fillcolor()} won, not the {user_bet} turtle...")
            return False
    return True


create_the_turtles()
position_the_turtles()

while race_on:
    race_on = run_turtles_race()

screen.exitonclick()
