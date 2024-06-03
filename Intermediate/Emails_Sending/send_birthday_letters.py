import datetime as dt
import json

import pandas
import random
from send_email import send_email

birthday_people = []
letters = {}

file = pandas.read_csv("data/birthdays.csv")
records = file.to_json(orient="records")
records = json.loads(records)

curr_year = dt.datetime.now().year
curr_month = dt.datetime.now().month
curr_day = dt.datetime.now().day
for record in records:
    print(record)
    if record["year"] == curr_year and record["month"] == curr_month and record["day"] == curr_day:
        birthday_people.append({"name": record["name"], "email": record["email"]})

for person in birthday_people:
    random_pick = random.randint(1, 3)
    if not letters.get(random_pick):
        with open(f"data/letters_templates/letter_{random_pick}.txt", mode="r") as file:
            letters[random_pick] = file.readlines()
    person["letter_number"] = random_pick

for person in birthday_people:
    letter_lines = letters[person["letter_number"]]
    letter = ""
    for line in letter_lines:
        if line.find("[NAME]"):
            letter += line.replace("[NAME]", person["name"])
        else:
            letter += line
    send_email(person["email"], f"Subject: Happy Birthday!!\n\n{letter}")
