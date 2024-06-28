import requests
from bs4 import BeautifulSoup
from price_email import send_low_price_email

ITEM_BASE_PRICE = 30
ITEM_NAME = "Loop-Quiet-Noise-Reduction-Earplugs"

user_headers = []

response = requests.get(url=f"https://www.amazon.com/{ITEM_NAME}/dp/B08MFDT65P")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
html_list = soup.find_all(name="span", class_="a-price-whole")
item_price = ""
for char in html_list[0].text:
    if char.isdigit():
        item_price += char
print(item_price)

if int(item_price) < ITEM_BASE_PRICE:
    send_low_price_email(ITEM_NAME.replace("-", " "), ITEM_BASE_PRICE, item_price)
