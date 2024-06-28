# Best Flight Deals Project

Welcome to the Best Flight Deals Project! This project allows you to track and notify users about flight deals using multiple APIs for data retrieval and notifications.

## Project Overview

The project fetches flight offers based on predefined criteria that can be reconfigured in the project code, updates the information in a Google Sheet, and notifies users via SMS and email if there are new flight deals.
## How It Works

1- Fetch Flight Data:
Retrieves flight data from the Amadeus API, searching for the lowest priced flights.

2- Update Google Sheet:
Uses the Sheety API to update flight information in a Google Sheet.

3- Notify Users:
Sends notifications via SMS using the Twilio API and emails using an SMTP server if a lower flight deal was found.

## Setup and Usage

a- Clone this repository to your local machine.

b- Obtain your API keys for Sheety, Amadeus, Twilio, and set up your SMTP server.

c- Add your API keys and other necessary credentials to a local `.env` file.

d- Ensure you have the following Python packages installed:
```bash
pip install requests python-dotenv
```

e- Execute the main Python script to start tracking flight deals:
```bash
python main.py
```

## *Enjoy the* ✈️ *!*
