# Weather SMS Notification Project

Welcome to the Weather SMS Notification Project! This project uses Twilio APIs to send an SMS alert to a phone number of your choice when the OpenWeather API forecasts rain within the next 12 hours.

## Project Overview

This project is designed to keep you informed about impending rainy weather by sending an SMS alert to your phone. By leveraging the OpenWeather API for weather data and the Twilio API for sending SMS messages, this project ensures you never get caught in the rain unprepared.

## How It Works

- Fetch Weather Data: The project fetches weather data for the next 12 hours using the OpenWeather API.

- Check for Rain: The weather data is checked for any forecasted rain.

- Send SMS Alert: If rain is forecasted, an SMS alert is sent to the specified phone number using the Twilio API.

## How to Use

1. Clone the repository.

2. Create an `.env` file and set up the keys and credentials needed.

3. Install the required packages:
    ```bash
    pip install requests twilio python-dotenv
    ```

4. Run the script:
    ```bash
    python main.py
    ```

## *Enjoy the* 🌧️ *!*