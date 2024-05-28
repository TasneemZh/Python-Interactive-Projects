import os.path
from turtle import Turtle

FILE_PATH = "./highest_score.txt"

RIGHT_ALIGNMENT = "left"
LEFT_ALIGNMENT = "right"
FONT = ('Arial', 14, 'normal')
FILE_PATH = "../../../../OneDrive/Desktop/highest_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.read_or_set_highest_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()
        self.update_highest_score()

    def read_or_set_highest_score(self):
        file_exists = os.path.exists(FILE_PATH)
        if file_exists:
            with open(FILE_PATH, "r") as file:
                file_content = file.read().strip()
                try:
                    self.highest_score = int(file_content)
                    return
                except ValueError:
                    self.highest_score = 0
            with open(FILE_PATH, "w") as file:
                file.write(str(self.highest_score))
            return

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}                                     ", align=LEFT_ALIGNMENT, font=FONT)
        self.write(f"                      Highest Score: {self.highest_score}", align=RIGHT_ALIGNMENT, font=FONT)

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("./highest_score.txt", "w") as file:
                file.write(str(self.highest_score))

    def display_game_over(self):
        self.update_highest_score()
        self.score = 0
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()
