import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv(".env")

parameters = {
    "appid": "9e0e07b7764d23db9cc1321517b3827b",
    "lat": "38.724660",
    "lon": "-89.401800",
    "cnt": 4
}

account_sid = os.environ.get("TWILIO_ACCOUNT_ID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
to_phone_number = os.environ.get("TO_PHONE_NUMBER")
from_phone_number = os.environ.get("FROM_PHONE_NUMBER")


def check_rainy_weather(weathers):
    for instance in weathers:
        for obj in instance["weather"]:
            if obj["id"] < 700:
                return True
    return False


client = Client(account_sid, auth_token)

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
list_of_weathers = response.json()["list"]
if check_rainy_weather(list_of_weathers):
    print("Bring an umbrela! It will rain in the next 12 hours!")
    message = client.messages.create(
        to=to_phone_number,
        from_=from_phone_number,
        body="Bring an umbrela! It will rain in the next 12 hours!")
    print(message.sid)
