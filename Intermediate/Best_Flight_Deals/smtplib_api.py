import os
import smtplib
from helpers import get_context
from dotenv import load_dotenv

load_dotenv(".env")


class Email:
    def __init__(self):
        self.sender_email = os.environ.get("SENDER_EMAIL")
        self.sender_password = os.environ.get("SENDER_PASSWORD")

    def send_flight_emails(self, flight_users, flight_data):
        user_emails = [flight_user["whatIsYourEmail?"] for flight_user in flight_users]
        for receiver in user_emails:
            with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(from_addr=self.sender_email, to_addrs=receiver,
                                msg=get_context(flight_data))
                server.quit()
            print("An email has been sent!")
