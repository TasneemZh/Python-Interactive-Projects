import requests
from bs4 import BeautifulSoup


def get_apartment_details():
    response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    apartments = []
    for a in soup.find_all("a", {"class": "StyledPropertyCardDataArea-anchor"}):
        property_dict = {}

        address = a.find("address", {"data-test": "property-card-addr"})
        if address:
            property_dict["address"] = address.text.strip()

        price = a.find_next("span", {"data-test": "property-card-price"})
        if price:
            property_dict["price"] = price.text.strip()

        link = a.get("href")
        if link:
            property_dict["link"] = link

        if "address" in property_dict and "price" in property_dict and "link" in property_dict:
            apartments.append(property_dict)

    print(f"properties: {apartments}")
    return apartments
