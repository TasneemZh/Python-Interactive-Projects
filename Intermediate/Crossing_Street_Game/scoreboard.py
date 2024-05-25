from turtle import Turtle

CENTER_ALIGNMENT = "center"
LEFT_ALIGNMENT = "right"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-140, 260)
        self.write(f"Level: {self.level}", align=LEFT_ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=LEFT_ALIGNMENT, font=FONT)

    def display_game_over(self):
        self.home()
        self.write("Game Over!", align=CENTER_ALIGNMENT, font=FONT)
