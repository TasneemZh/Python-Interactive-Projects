import requests
import time
from datetime import datetime
from send_email import send_email

LAN_VALUE = "17.19957160297496"
LONG_VALUE = "1.558958888053894"


def is_iss_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_location = iss_response.json()["iss_position"]
    iss_latitude = float(iss_location["latitude"])
    iss_longitude = float(iss_location["longitude"])

    if (abs(float(LAN_VALUE) - iss_latitude) <= 5) and (abs(float(LONG_VALUE) - iss_longitude) <= 5):
        return True
    return False


def is_night():
    parameters = {
        "lat": LAN_VALUE,
        "lng": LONG_VALUE,
        "formatted": "0"
    }

    response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    response_formatted = response.json()["results"]
    sunrise = response_formatted["sunrise"]
    sunset = response_formatted["sunset"]
    sunrise_hour = datetime.fromisoformat(sunrise).hour
    sunset_hour = datetime.fromisoformat(sunset).hour
    curr_hour = datetime.now().hour
    if sunrise_hour >= curr_hour >= sunset_hour:
        return True
    return False


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email("example@gmail.com",
                   "Subject: It is Time!\n\nLook up at the sky~~\n\nSweet Dreams 💤")
