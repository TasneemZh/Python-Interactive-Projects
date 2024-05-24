from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("purple")
        self.penup()
        self.y = 10
        self.x = 10

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def handle_boarders_collision(self):
        if abs(int(self.ycor())) >= 330:
            self.bounce('y')

    def handle_paddles_collision(self, paddle):
        print(f"distance: {int(self.distance(paddle))}")
        if int(self.distance(paddle)) <= 40:
            self.bounce('x')
            return True
        return False

    def bounce(self, coordinator):
        if coordinator == 'x':
            self.x *= -1
        elif coordinator == 'y':
            self.y *= -1

    def check_if_ball_escaped(self):
        print(f"x: {self.xcor()}")
        if abs(self.xcor()) >= 320:
            return True
        return False
