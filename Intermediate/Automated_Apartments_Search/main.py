from apartments import get_apartment_details
from forms import Form

form_instance = Form()

apartments = get_apartment_details()

for apartment in apartments:
    form_instance.fill_form(apartment)

# To view the data in a table format:
# https://docs.google.com/spreadsheets/d/1m3x2-AsrnZ7g7h3rNmTcm0soJ0v9TCuhaeQJ47_BGTw/edit?usp=sharing