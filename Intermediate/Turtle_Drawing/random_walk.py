from turtle import Turtle, Screen
import random

bob = Turtle()
screen = Screen()

screen.colormode(255)
bob.shape("turtle")
bob.width(5)


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    bob.pencolor((r, g, b))


def go_right():
    bob.right(90)


def go_left():
    bob.left(90)


directions = {
    "right": "go_right",
    "left": "go_left"
}

while True:
    generate_random_color()
    random.choice([go_right, go_left])()
    bob.forward(20)
