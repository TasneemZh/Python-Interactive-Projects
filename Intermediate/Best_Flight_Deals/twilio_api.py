import os
from twilio.rest import Client
from helpers import get_context
from dotenv import load_dotenv

load_dotenv(".env")


class Twilio:
    def __init__(self):
        account_sid = os.environ.get("TWILIO_ACCOUNT_ID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.to_phone_number = os.environ.get("TO_PHONE_NUMBER")
        self.from_phone_number = os.environ.get("FROM_PHONE_NUMBER")
        self.client = Client(account_sid, auth_token)

    def send_sms_message(self, flight_data):
        message = self.client.messages.create(
            to=self.to_phone_number,
            from_=self.from_phone_number,
            body=get_context(flight_data))
        print(message.sid)
