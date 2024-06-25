from datetime import datetime


def get_context(flight_data):
    departure_date_at = datetime.strptime(flight_data["departure_date_at"], "%Y-%m-%dT%H:%M:%S")
    arrival_date_at = datetime.strptime(flight_data["arrival_date_at"], "%Y-%m-%dT%H:%M:%S")

    departure_formatted = departure_date_at.strftime("%Y-%m-%d")
    arrival_formatted = arrival_date_at.strftime("%Y-%m-%d")

    message = (
        f"\nLow price alert! Only {flight_data["min_price"]} to fly from {flight_data["origin"]} "
        f"to {flight_data["destination"]}, on {departure_formatted} until {arrival_formatted}.")
    return message
