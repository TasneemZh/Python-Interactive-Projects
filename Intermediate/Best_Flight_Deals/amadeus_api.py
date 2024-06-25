import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")


class Amadeus:

    def __init__(self):
        self.base_url = "https://test.api.amadeus.com"
        self.flight = None
        self.set_flight_data({})

    def generate_auth_token(self):
        token_url = f"{self.base_url}/v1/security/oauth2/token"
        response = requests.post(
            url=token_url,
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "grant_type": "client_credentials",
                "client_id": os.environ.get("AMADEUS_API_KEY"),
                "client_secret": os.environ.get("AMADEUS_API_SECRET")
            })
        response.raise_for_status()
        print("generate_auth_token")
        headers = {
            "Authorization": f"Bearer {response.json()["access_token"]}"
        }
        return headers

    def get_flight_city_code(self, city_name):
        headers = self.generate_auth_token()
        parameters = {
            "keyword": city_name,
            "max": "1",
            "include": "AIRPORTS",
        }
        url = f"{self.base_url}/v1/reference-data/locations/cities"
        response = requests.get(url=url, headers=headers, params=parameters)
        response.raise_for_status()
        return response.json()["data"][0]["iataCode"]

    def set_flight_offers(self, destination_code, departure_date, return_date, non_stop):
        url = f"{self.base_url}/v2/shopping/flight-offers"
        parameters = {
            "originLocationCode": "LON",
            "destinationLocationCode": destination_code,
            "adults": "1",
            "currencyCode": "GBP",
            "departureDate": departure_date,
            "returnDate": return_date,
            "nonStop": non_stop
        }
        headers = self.generate_auth_token()
        response = requests.get(url=url, headers=headers, params=parameters)
        response.raise_for_status()
        print(f"set_flight_offers")
        return response.json()

    def check_indirect_flights(self, response_json, destination_code, departure_date, return_date):
        try:
            if not len(response_json["data"]):
                indirect_json = self.set_flight_offers(destination_code, departure_date, return_date, "false")
                return {"response": indirect_json, "is_indirect": True}
            return {"response": response_json, "is_indirect": False}
        except Exception as error:
            print(f"Oops in indirect flights! There's an error...\n{error}")
            return {"response": None, "is_indirect": None}

    def set_flight_data(self, offer_data):
        try:
            self.flight["min_price"] = float(offer_data["price"]["grandTotal"])
            self.flight["origin"] = offer_data["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            self.flight["destination"] = offer_data["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            self.flight["departure_date_at"] = offer_data["itineraries"][0]["segments"][0]["departure"]["at"]
            self.flight["arrival_date_at"] = offer_data["itineraries"][0]["segments"][0]["arrival"]["at"]
        except KeyError:
            self.flight = {
                "min_price": None,
                "origin": None,
                "destination": None,
                "departure_date_at": None,
                "arrival_date_at": None
            }

    def set_indirect_flight_data(self, offer_data):
        segments = offer_data["itineraries"][0]["segments"]
        self.flight["min_price"] = float(offer_data["price"]["grandTotal"])
        self.flight["origin"] = segments[0]["departure"]["iataCode"]
        self.flight["destination"] = segments[len(segments) - 1]["arrival"]["iataCode"]
        self.flight["departure_date_at"] = segments[0]["departure"]["at"]
        self.flight["arrival_date_at"] = segments[len(segments) - 1]["arrival"]["at"]

    def get_flight_offers(self, destination_code, departure_date, return_date, min_price=None):
        try:
            response_json = self.set_flight_offers(destination_code, departure_date, return_date, "true")
            final_response = self.check_indirect_flights(response_json, destination_code, departure_date, return_date)

            response_json = final_response["response"]
            is_indirect = final_response["is_indirect"]

            for flight_offer in response_json["data"]:
                if float(flight_offer["price"]["grandTotal"]) < min_price:
                    if is_indirect:
                        self.set_indirect_flight_data(flight_offer)
                    else:
                        self.set_flight_data(flight_offer)
            return self.flight
        except Exception as error:
            print(f"Oops in flights handler! There's an error...\n{error}")
            self.set_flight_data({})
            return self.flight
