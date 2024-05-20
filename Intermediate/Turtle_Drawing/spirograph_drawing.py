from turtle import Turtle, Screen
from constants import colors_palette

bob = Turtle()
screen = Screen()

bob.shape("arrow")
bob.speed(100)


def draw_spirograph(shift):
    index = 0
    for _ in range(int(360/shift)):
        bob.color(colors_palette[index % len(colors_palette)])
        index += 1
        bob.circle(100)
        bob.setheading(bob.heading() + shift)


draw_spirograph(5)

screen.exitonclick()
