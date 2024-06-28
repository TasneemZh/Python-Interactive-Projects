import os
import smtplib
from dotenv import load_dotenv

load_dotenv(".env")

sender_email = os.environ.get("SENDER_EMAIL")
sender_password = os.environ.get("SENDER_PASSWORD")


def send_low_price_email(user_item, original_price, item_price):
    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(from_addr=sender_email, to_addrs=sender_email,
                        msg=f"Subject: Amazon Item - Low Price Alert!\n\n"
                            f"The item {user_item} has dropped from {original_price} to {item_price}!")
        server.quit()
    print("An email has been sent!")
