import json
import random
import pandas
import tkinter
from tkinter import Tk, Canvas, Button

BG_COLOR = "#DBB5B5"
FILL_COLOR_1 = "#254336"
FILL_COLOR_2 = "#6B8A7A"
TEXT_COLOR_1 = "#B7B597"
TEXT_COLOR_2 = "#DAD3BE"
FONT_PROPERTIES = ("Arial", 40, "bold")

french_rectangle = None
english_rectangle = None


def flip_card(show_french=True):
    global english_rectangle
    global french_rectangle
    if show_french:
        canvas.delete(english_rectangle)
        canvas.create_rectangle(200, 200, 200, 200)
        canvas.configure(bg=FILL_COLOR_1, highlightthickness=0)
        french_rectangle = canvas.create_text(200, 200, text=french_words[index], fill=TEXT_COLOR_1,
                                              font=FONT_PROPERTIES)
        window.after(3000, flip_card, False)
    else:
        canvas.delete(french_rectangle)
        canvas.create_rectangle(200, 200, 200, 200)
        canvas.configure(bg=FILL_COLOR_2, highlightthickness=0)
        english_rectangle = canvas.create_text(200, 200, text=english_words[index], fill=TEXT_COLOR_2,
                                               font=FONT_PROPERTIES)


def remove_pair():
    global index
    with open("data/known_words.csv", mode="a") as file:
        file.write(f"{french_words[index]},{english_words[index]}\n")
    data_frame = pandas.DataFrame({
        "French": french_words[0: index] + french_words[index + 1:],
        "English": english_words[0: index] + english_words[index + 1:]
    })
    data_frame.to_csv("data/flash_cards_word.csv", index=False, mode="w")

    latest_read = pandas.read_csv("data/flash_cards_word.csv")
    words = latest_read["French"].tolist()
    index = random.randint(0, len(words))
    flip_card()


def pick_random_index():
    global index
    index = random.randint(0, len(french_words))
    flip_card()


words_file = pandas.read_csv("data/flash_cards_word.csv")
french_words = words_file["French"].tolist()
english_words = words_file["English"].tolist()
index = random.randint(0, len(french_words))

window = Tk()
window.configure(bg=BG_COLOR, padx=100, pady=20)
window.minsize(600, 600)
window.title("Flash Cards")
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=2)
window.after(3000, flip_card, False)

canvas = Canvas(window, width=400, height=400, bg=BG_COLOR, highlightthickness=0)
canvas.create_rectangle(200, 200, 200, 200)
canvas.configure(bg=FILL_COLOR_1, highlightthickness=0)
french_rectangle = canvas.create_text(200, 200, text=french_words[index], fill=TEXT_COLOR_1, font=FONT_PROPERTIES)
canvas.grid(column=0, row=0, columnspan=3)

check_mark = tkinter.PhotoImage(file="images/check_mark.png")
cross_mark = tkinter.PhotoImage(file="images/cross_mark.png")

right_btn = Button(image=check_mark, bg=BG_COLOR, highlightthickness=0, borderwidth=0,
                   command=remove_pair)
right_btn.grid(column=0, row=1)
cancel_btn = Button(image=cross_mark, bg=BG_COLOR, highlightthickness=0, borderwidth=0,
                    command=pick_random_index)
cancel_btn.grid(column=2, row=1)

window.mainloop()
