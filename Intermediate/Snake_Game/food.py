import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(1)
        self.color("white")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-180, 180)
        rand_y = random.randint(-180, 180)
        self.goto(rand_x, rand_y)
