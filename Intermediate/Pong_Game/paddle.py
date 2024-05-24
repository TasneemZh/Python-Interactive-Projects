from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("pink")
        self.put_in_place(direction)
        self.speed("fastest")

    def put_in_place(self, direction):
        if direction == "right":
            self.goto(250, 0)
            self.showturtle()
        elif direction == "left":
            self.goto(-250, 0)
            self.showturtle()
        else:
            self.goto(0, 0)
            self.showturtle()

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
