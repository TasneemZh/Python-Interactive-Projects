import math
import tkinter
from tkinter import Tk, Button, Label, Canvas

BG_COLOR = "#EEE5E5"
PAYNE_GRAY = "#19647E"
VERDIGRIS = "#28AFB0"
BLACK_OLIVE = "#37392E"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3

session = 1
work_sessions = 1
timer_window = None


def reset():
    global session
    global work_sessions
    window.after_cancel(timer_window)
    session = 1
    work_sessions = 1
    canvas.itemconfigure(timer_counter, text="00:00")
    label_tick.configure(text="")
    label.configure(text="Timer", fg=PAYNE_GRAY)


def count_down(count=WORK_MIN * 60):
    global session
    global work_sessions
    global timer_window
    if session == 1:
        label.configure(text="Work", fg="green")
    if count >= 0:
        timer_window = window.after(1000, display_timer, count)
    else:
        session += 1
        if session == 8:
            label.configure(text="Break", fg="red")
            count_down(LONG_BREAK_MIN * 60)
            session = 0
        elif session % 2 == 0:
            label.configure(text="Break", fg="pink")
            check_marks = ""
            for _ in range(work_sessions):
                check_marks += "✔️"
            label_tick.configure(text=check_marks)
            count_down(SHORT_BREAK_MIN * 60)
        else:
            work_sessions += 1
            label.configure(text="Work", fg="green")
            count_down()


def display_timer(count):
    min_counter = math.floor(count / 60)
    sec_counter = count % 60
    if sec_counter < 10:
        sec_counter = f"0{sec_counter}"
    canvas.itemconfigure(timer_counter, text=f"{min_counter}:{sec_counter}")
    count -= 1
    count_down(count)


window = Tk()
window.config(bg=BG_COLOR, width=1000, height=1000, padx=30, pady=30)
window.title("Pomodoro Timer")

canvas = Canvas()
image = tkinter.PhotoImage(file="tomato.png")
resized_image = image.subsample(2, 2)
canvas.create_image(180, 100, image=resized_image)
timer_counter = canvas.create_text(180, 125, fill=BLACK_OLIVE, text="00:00", font=(FONT_NAME, 28, "bold"))
canvas.configure(bg=BG_COLOR, highlightthickness=0)
canvas.grid_configure(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=BG_COLOR, fg=PAYNE_GRAY)
label.grid_configure(column=1, row=0)

start_button = Button(text="START", bg=VERDIGRIS, width=6, height=2, foreground="red", font=(FONT_NAME, 10, "bold"),
                      command=count_down)
start_button.grid_configure(column=0, row=2)

reset_button = Button(text="RESET", bg=VERDIGRIS, width=6, height=2, foreground="red", font=(FONT_NAME, 10, "bold"),
                      command=reset)
reset_button.grid_configure(column=2, row=2)

label_tick = Label(font=(FONT_NAME, 15, "bold"), bg=BG_COLOR, fg="black")
label_tick.grid_configure(column=1, row=3)

window.mainloop()
