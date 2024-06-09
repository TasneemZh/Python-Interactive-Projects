import os
from twilio.rest import Client
from constants import STOCK


def send_sms_message(article, stock_percent, is_diff_higher):
    account_sid = os.environ.get("TWILIO_ACCOUNT_ID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    to_phone_number = os.environ.get("TO_PHONE_NUMBER")
    from_phone_number = os.environ.get("FROM_PHONE_NUMBER")

    client = Client(account_sid, auth_token)

    if is_diff_higher:
        icon = "🔺"
    else:
        icon = "🔻"

    message = client.messages.create(
        to=to_phone_number,
        from_=from_phone_number,
        body=f"{STOCK}: {icon}{stock_percent}%\n"
             f"Headline: {article["title"]}\n"
             f"Brief: {article["description"]}")
    print(message.sid)
