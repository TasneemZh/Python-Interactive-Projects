import json
import tkinter
from tkinter import Tk, Canvas, Label, Entry, Button, messagebox
from password_generator import generate_password

FONT_NAME = "Arial"
LABEL_TEXT_COLOR = "black"
BG_COLOR = "white"
FONT = (FONT_NAME, 9, "bold")


def paste_from_clipboard():
    generate_password(window)
    textbox3.delete(0, tkinter.END)
    textbox3.insert(0, window.clipboard_get())


def search_data_file():
    company = textbox1.get()
    try:
        with open("user_data.json", mode="r") as file:
            json_data = json.load(file)
            try:
                messagebox.showinfo(title=company, message=f"Email: {json_data[company]["Email"]}\n"
                                                           f"Password: {json_data[company]["Password"]}")
            except KeyError:
                messagebox.showwarning(title="Not Found", message=f"{company} was not found!")
    except FileNotFoundError:
        messagebox.showwarning(title="Not Found", message=f"No date file found!")


def write_data_to_file():
    input1 = textbox1.get()
    input2 = textbox2.get()
    input3 = textbox3.get()

    is_okay = False

    if not input1 or not input2 or not input3:
        messagebox.showwarning(title="Empty fields!", message="You can't leave any field empty!")
    else:
        is_okay = messagebox.askokcancel(title=input1, message=f"Here are your details:\n"
                                                               f"Email: {input2}\n"
                                                               f"Password: {input3}\n\n"
                                                               f"Is it okay to save them?")

    if is_okay:
        try:
            with open("user_data.json", mode="r") as file:
                json_data = json.load(file)
                json_data.update({
                    input1: {
                        "Email": input2,
                        "Password": input3
                    }
                })
                with open("user_data.json", mode="w") as file:
                    json.dump(json_data, file, indent=4)
        except FileNotFoundError:
            with open("user_data.json", mode="w") as file:
                json_data = {
                    input1: {
                        "Email": input2,
                        "Password": input3
                    }
                }
                json.dump(json_data, file, indent=4)

        textbox1.delete(0, tkinter.END)
        textbox3.delete(0, tkinter.END)

        textbox1.focus()


window = Tk()
canvas = Canvas()

window.title("Passwords Locker 🔒")
window.configure(padx=30, pady=30, bg="white")

window.minsize(width=500, height=400)

image = tkinter.PhotoImage(file="locker.png")
mini_image = image.subsample(2, 2)
image_width = mini_image.width()
image_height = mini_image.height()

canvas.config(width=image_width, height=image_height + 50, bg="white", highlightthickness=0)
canvas.create_image(image_width / 1.2, image_height // 2, image=mini_image)
canvas.grid(column=1, row=0, sticky="nsew")

label1 = Label(text="Website:", font=FONT, bg=BG_COLOR, fg=LABEL_TEXT_COLOR)
label1.grid(column=0, row=1, sticky="w")

label2 = Label(text="Email/Username:", font=FONT, bg=BG_COLOR, fg=LABEL_TEXT_COLOR)
label2.grid(column=0, row=2, sticky="w")

label3 = Label(text="Password:", font=FONT, bg=BG_COLOR, fg=LABEL_TEXT_COLOR)
label3.grid(column=0, row=3, sticky="w")

textbox1 = Entry(width=21, border=2)
textbox1.focus()
textbox1.grid(column=1, row=1, sticky="ew")

textbox2 = Entry(width=35, border=2)
textbox2.grid(column=1, row=2, columnspan=2, sticky="ew")
textbox2.insert(0, "example@gmail.com")

textbox3 = Entry(width=21, border=2)
textbox3.grid(column=1, row=3, sticky="ew")

search_btn = Button(text="Search", background=BG_COLOR, font=FONT, command=search_data_file)
search_btn.grid(column=2, row=1, sticky="ew")

generator_btn = Button(text="Generate Password", background=BG_COLOR, font=FONT, command=paste_from_clipboard)
generator_btn.grid(column=2, row=3, sticky="ew")

add_btn = Button(text="Add", background=BG_COLOR, font=FONT, command=write_data_to_file)
add_btn.grid(column=1, row=4, columnspan=2, sticky="ew")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight=1)

for i in range(0, 5):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()
