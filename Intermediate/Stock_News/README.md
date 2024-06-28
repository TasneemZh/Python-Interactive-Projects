# Stock News Alert Project

Welcome to the Stock News Alert Project! This project monitors stock price changes and sends news alerts if significant changes are detected.

## Project Overview

This project checks for a 5% increase or decrease in a stock's price between yesterday and the day before yesterday. If such a change is detected, it fetches the latest news articles related to the company and sends the news headlines and brief descriptions via SMS.

## How It Works

- Check Stock Price:

    Uses the Alpha Vantage API to get the closing stock prices for yesterday and the day before yesterday.


- Calculates the percentage change:

    If it is greater than or equal to 5%, it proceeds to fetch news articles.


- Fetch News Articles:

    Uses the News API to get the top 3 latest news articles related to the company.


- Send SMS Alerts:

    Uses the Twilio API to send an SMS with the article titles and brief descriptions to a specified phone number.

## Setup and Usage

1. Clone this repository to your local machine.

2. Sign up and get your API keys for Alpha Vantage, News API, and Twilio.

3. Set your API keys in a `.env` file in the root level of your project.

4. Ensure you have the following Python packages installed:

    ```bash
    pip install requests twilio python-dotenv
    ```

5. Run the following script:
    ```bash
    python main.py.py
    ```

## *Enjoy the* 📰 *!*
