import random
import datetime as dt
from send_email import send_email


def pick_random_quote():
    with open("data/quotes.txt", mode="r", encoding="utf-8", errors="replace") as file:
        lines = file.readlines()
        return random.choice(lines)


if dt.datetime.now().weekday() == 0:
    print("It is Monday!!!")
    quote = pick_random_quote()
    email_context = "Subject:Motivational Quote For the Day!\n\n"
    + "Hello dear,\n\n"
    + f"{quote}\nRegards,"
    send_email("test@gmail.com", email_context)
