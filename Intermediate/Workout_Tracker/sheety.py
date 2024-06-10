import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(".env")


def create_workout_record(exercise, duration, calories):
    endpoint = f"https://api.sheety.co/{os.environ.get("SHEETY_USER_ID")}/workoutTracker/workouts"

    headers = {
        "Authorization": f"Bearer {os.environ.get("SHEETY_AUTH_TOKEN")}"
    }

    date = datetime.now()
    today_date = date.strftime("%Y-%m-%d %H:%M:%S")
    today_date_list = today_date.split(" ")

    payload = {
        "workout": {
            "date": today_date_list[0],
            "time": today_date_list[1],
            "exercise": exercise,
            "duration": str(duration),
            "calories": calories
        }
    }

    response = requests.post(url=endpoint, json=payload, headers=headers)
    response.raise_for_status()
    print(response.json())
