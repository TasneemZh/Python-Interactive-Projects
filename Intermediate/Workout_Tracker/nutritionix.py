import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")


def get_user_workouts():
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    headers = {
        "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
        "x-app-key": os.environ.get("NUTRITIONIX_APP_KEY")
    }

    payload = {
        "query": input("What exercise did you do today? ")
    }

    response = requests.post(url=endpoint, json=payload, headers=headers)
    response.raise_for_status()
    print(response.json()["exercises"])

    return response.json()["exercises"]
