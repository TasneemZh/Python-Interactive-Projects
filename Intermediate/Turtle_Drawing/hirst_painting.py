from turtle import Turtle, Screen
import colorgram
import random

rgb_list = []

colors = colorgram.extract('colorful_dots.jpg', 40)
for color_group in colors:
    rgb_list.append((color_group.rgb[0], color_group.rgb[1], color_group.rgb[2]))

for index in range(5):
    rgb_list.pop(index)

bob = Turtle()
screen = Screen()

bob.shape("arrow")
bob.speed(100)
screen.colormode(255)


def move_to_bottom_right():
    bob.penup()
    bob.right(180)
    bob.forward(250)
    bob.left(90)
    bob.forward(200)
    bob.left(90)


def draw_colorful_dot():
    bob.pendown()
    color_index = random.randint(0, len(rgb_list)-1)
    color = rgb_list[color_index % len(rgb_list)]
    while color == (255, 255, 255):
        color = rgb_list[color_index % len(rgb_list)]
    return color


def draw_spots():
    for column in range(10):
        for row in range(10):
            color = draw_colorful_dot()
            bob.dot(20, color)
            bob.penup()
            bob.forward(50)
        bob.backward(50)
        if column % 2 != 0:
            bob.right(90)
            bob.forward(50)
            bob.right(90)
        else:
            bob.left(90)
            bob.forward(50)
            bob.left(90)
        bob.pendown()


move_to_bottom_right()
draw_spots()
screen.exitonclick()
