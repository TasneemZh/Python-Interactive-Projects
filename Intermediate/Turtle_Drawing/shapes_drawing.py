from constants import colors
from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

bob.shape("turtle")


def centralize_turtle():
    bob.penup()
    bob.forward(100)
    bob.pendown()


def draw_shapes():
    index = 0
    for shape in range(2, 10):
        bob.color(colors[index])
        index += 1
        angle = round(360/(shape+1), 2)
        for _ in range(shape):
            bob.right(angle)
            bob.forward(100)
        bob.right(angle)
        centralize_turtle()


bob.forward(100)
draw_shapes()
screen.exitonclick()
