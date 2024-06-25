import json
import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")


class Sheety:

    def __init__(self):
        self.endpoint = f"https://api.sheety.co/{os.environ.get("SHEETY_USER_ID")}/flightDeals"
        self.headers = {
            "Authorization": f"Bearer {os.environ.get("SHEETY_BEARER_TOKEN")}"
        }

    def get_sheet_data(self, data_type):
        response = requests.get(url=f"{self.endpoint}/{data_type}", headers=self.headers)
        response.raise_for_status()
        return response.json()[data_type]

    def edit_sheet_data(self, record_id, new_data, data_type):
        response = requests.put(url=f"{self.endpoint}/{data_type}/{record_id}", json={
            "price": new_data
        }, headers=self.headers)
        response.raise_for_status()
