import pandas
from turtle import Turtle, Screen


screen = Screen()
states_data = pandas.read_csv("50_states.csv")

screen.title("Guess The States Game 🌍")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

STATES_COUNT = 50
count = 0
guessed_states = []

while count < STATES_COUNT:
    user_state = screen.textinput(f" {count}/{STATES_COUNT} Correct States", "Enter a state name:").lower()
    if user_state == "exit":
        break
    is_found = states_data[states_data["state"].str.lower() == user_state]
    states_found = is_found["state"].str.lower()

    if user_state in states_found.values:
        guessed_states.append(user_state)
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(is_found["x"].values[0], is_found["y"].values[0])
        turtle.write(is_found["state"].values[0], align="center", font=("Arial", 10, "normal"))
        count += 1

if count < STATES_COUNT:
    all_states_lower = states_data["state"].str.lower()
    all_states = all_states_lower.values
    missed = [state for state in all_states if state not in guessed_states]
    missed_data = pandas.DataFrame({"Missed Sates": [i.title() for i in missed]})
    missed_data.to_csv("missed_states.csv")

screen.mainloop()
