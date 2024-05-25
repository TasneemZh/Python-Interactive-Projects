from turtle import Turtle

CENTER_ALIGNMENT = "center"
RIGHT_ALIGNMENT = "left"
LEFT_ALIGNMENT = "right"
FONT = ('Verdana', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()
        self.update_score()
        self.split_the_screen()

    def increase(self, direction):
        if direction == "right":
            self.right_score += 1
        else:
            self.left_score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"  {self.right_score}  ", align=RIGHT_ALIGNMENT, font=FONT)
        self.write(f"  {self.left_score}  ", align=LEFT_ALIGNMENT, font=FONT)

    def display_game_over(self):
        self.home()
        self.write("Game Over!", align=CENTER_ALIGNMENT, font=FONT)

    @staticmethod
    def split_the_screen():
        pen = Turtle()
        pen.color("white")
        pen.shape("arrow")
        pen.hideturtle()
        pen.penup()
        pen.goto(0, 350)
        pen.setheading(270)
        pen.pendown()
        pen.forward(700)
