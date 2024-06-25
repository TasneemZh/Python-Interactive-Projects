from sheety_api import Sheety
from amadeus_api import Amadeus
from twilio_api import Twilio
from smtplib_api import Email
from datetime import datetime, timedelta

sheet = Sheety()
flight = Amadeus()
twilio = Twilio()
email = Email()

flight_records = sheet.get_sheet_data("prices")

for record in flight_records:
    airport_code = flight.get_flight_city_code(city_name=record["city"])
    sheet.edit_sheet_data(record_id=record["id"], new_data={
        "city": record["city"],
        "iataCode": airport_code,
        "lowestPrice": record["lowestPrice"]
    }, data_type="prices")
    min_price = None
    if airport_code:
        min_price = float(record["lowestPrice"])
        tomorrow = datetime.now() + timedelta(days=1)
        six_months_after = datetime.now() + timedelta(days=6 * 30)
        flight_data = flight.get_flight_offers(
            destination_code=airport_code,
            departure_date=tomorrow.strftime("%Y-%m-%d"),
            return_date=six_months_after.strftime("%Y-%m-%d"),
            min_price=min_price,
        )
        if flight_data["min_price"]:
            print(f"Min Price: {flight_data["min_price"]}, City: {record['city']}")
            if flight_data["min_price"] != float(record["lowestPrice"]):
                twilio.send_sms_message(flight_data)
                flight_users = sheet.get_sheet_data("users")
                email.send_flight_emails(flight_users, flight_data)
    if not min_price:
        print("N/A")
