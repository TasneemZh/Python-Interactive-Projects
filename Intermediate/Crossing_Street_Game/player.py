from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.set_turtle_position()

    def set_turtle_position(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def cross_a_street(self):
        self.forward(MOVE_DISTANCE)

    def reached_the_end(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.set_turtle_position()
            return True
        return False
