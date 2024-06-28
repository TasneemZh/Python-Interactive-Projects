# Amazon Item Price Notifier

This project checks the price of a specific item on Amazon and sends an email alert if the price drops below a set threshold. It demonstrates **Web Scraping**.

## Project Overview

This project scrapes Amazon for the price of a specified item and triggers an email alert if the price drops below a specified base price.

## How It Works

1. **Price Check**:
   - The script scrapes the Amazon page of the specified item using `BeautifulSoup`.
   - It extracts the current price of the item.
   - If the current price is below the specified base price, an email alert is triggered.

2. **Email Alert**:
   - The script sends an email using the `smtplib` library.
   - The email includes the item name, the original price, and the current low price.

## Setup and Installation

### Prerequisites

- Python 3.x
- `requests` library
- `BeautifulSoup` from `bs4`
- `python-dotenv` library for managing environment variables

### Installation

1. Clone the repository.

2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 python-dotenv
   ```

3. Create a `.env` file in the project directory and add your email credentials:
   ```env
   SENDER_EMAIL=your_email@gmail.com
   SENDER_PASSWORD=your_password
   ```

## Usage

1. **Configure the item and base price**:
   - In `main.py`, set the `ITEM_BASE_PRICE` and `ITEM_NAME` variables.
2. **Run the script**:
   ```bash
   python main.py
   ```

3. If the item price is below the base price, an email alert will be sent to the configured email address.

## License

This project is licensed under the MIT License.

## *Enjoy the* 🤑 *!*