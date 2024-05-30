import tkinter
from tkinter import Tk, Button, Entry, Label

KM_IM_MILES = 1.609344
FONT_PROPERTIES = ("Arial", 14)

window = Tk()
window.config(bg="white", width=600, height=600, padx=30, pady=30)
window.title("Miles Converter")


def convert_miles_to_kilometers():
    miles = float(user_input.get())
    print(miles)
    user_input.delete(0, tkinter.END)
    km = round(miles * KM_IM_MILES, 2)
    label3.config(text=km)


button = Button(text="Calculate", highlightcolor="red", command=convert_miles_to_kilometers, width=8, height=1,
                font=FONT_PROPERTIES, bg="white")
button.configure(pady=5)
button.grid_configure(column=1, row=2)

user_input = Entry(width=15, border="2")
user_input.grid_configure(column=1, row=0)

label1 = Label(text="Miles", bg="white", font=FONT_PROPERTIES)
label1.grid_configure(column=2, row=0)

label2 = Label(text="is equal to", bg="white", pady=15, font=FONT_PROPERTIES)
label2.grid_configure(column=0, row=1)

label3 = Label(text="0", bg="white", font=FONT_PROPERTIES)
label3.grid_configure(column=1, row=1)

label4 = Label(text="Km", bg="white", font=FONT_PROPERTIES)
label4.grid_configure(column=2, row=1)

window.mainloop()
