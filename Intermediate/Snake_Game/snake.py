import time
from turtle import Turtle

MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            bob = self.paint_snake()
            self.turtles.append(bob)
            self.turtles[i].goto(-1 * x, y)
            x += 20

    @staticmethod
    def paint_snake():
        bob = Turtle()
        bob.color("#D2649A")
        bob.shape("square")
        bob.penup()
        return bob

    def move(self):
        for part in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[part - 1].xcor()
            y = self.turtles[part - 1].ycor()
            self.turtles[part].goto(x, y)
        self.head.forward(MOVING_DISTANCE)

    def check_collide_with_boarders(self):
        x = self.head.xcor()
        y = self.head.ycor()
        print(f"x: {x}, abs: {abs(int(x))}, y: {y}, abs: {abs(int(y))}")
        if abs(int(x)) >= (300 - 10) or abs(int(y)) >= (300 - 10):
            return False
        return True

    def check_collide_with_body(self):
        for part in self.turtles[1:]:
            if self.head.distance(part) < 10:
                return False
        return True

    def grow(self):
        bob = self.paint_snake()
        last_part = len(self.turtles) - 1
        x = self.turtles[last_part].xcor()
        y = self.turtles[last_part].ycor()
        bob.goto(x, y)
        self.turtles.append(bob)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
