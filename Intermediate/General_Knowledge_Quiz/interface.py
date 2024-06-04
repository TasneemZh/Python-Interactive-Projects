import tkinter
from tkinter import Tk, Canvas, Button, Label
from quiz_brain import QuizBrain

BG_COLOR = "#8789C0"
BOARD_COLOR = "#AF4D98"
FONT_COLOR = "#9DF7E5"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Test Your Knowledge 🧠")
        self.window.configure(padx=20, pady=20, bg=BG_COLOR)
        self.window.minsize(width=340, height=500)

        self.label = Label(text=f"          Score: {self.score}", font=("Arial", 14, "normal"), bg=BG_COLOR, fg="white")
        self.label.grid_configure(column=1, row=0)

        self.board = Canvas()
        self.board.create_rectangle(20, 20, 20, 20)
        self.board.configure(width=300, height=250, bg=BOARD_COLOR, highlightthickness=0)
        self.question = self.board.create_text(150, 125, font=("Arial", 16, "normal"), fill=FONT_COLOR,
                                               text="First Question!", width=280)
        self.board.grid_configure(column=0, row=1, columnspan=2)

        check_mark = tkinter.PhotoImage(file="images/check_mark.png")
        cross_mark = tkinter.PhotoImage(file="images/cross_mark.png")

        self.true_btn = Button(image=check_mark, bg=BG_COLOR, highlightthickness=0, borderwidth=0,
                           command=self.is_true)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=cross_mark, bg=BG_COLOR, highlightthickness=0, borderwidth=0,
                            command=self.is_false)
        self.false_btn.grid(column=1, row=2)

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=2)

        self.display_next_question()

        self.window.mainloop()

    def display_next_question(self):
        question_text = self.quiz_brain.next_question()
        self.board.itemconfigure(self.question, text=question_text)

    def is_true(self):
        is_right = self.quiz_brain.check_answer("true")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz_brain.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            color = "green"
            self.score += 1
            self.label.configure(text=f"          Score: {self.score}")
        else:
            color = "red"
        self.board.configure(bg=color)
        self.window.after(1000, self.reset_board_color)

    def reset_board_color(self):
        self.board.configure(bg=BOARD_COLOR)
        QuizBrain.question_number += 1
        if self.quiz_brain.still_has_questions():
            self.display_next_question()
        else:
            self.board.itemconfigure(self.question, text="The End!!!")
            self.true_btn.configure(state="disabled")
            self.false_btn.configure(state="disabled")
