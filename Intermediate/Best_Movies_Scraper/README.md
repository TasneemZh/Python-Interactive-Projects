# Best Movies Scraper Project

Welcome to the Best Movies Scraper Project! This project scrapes the list of best movies from Empire Online and saves it to a text file.

## Project Overview

The Best Movies Scraper Project uses **Web Scraping** to extract movie titles and their ranks from a real website. It then saves this information to a text file in a structured format.

## How It Works

1️⃣ Fetch Webpage:
Uses the `requests` library to fetch the content of the webpage containing the list of best movies.

2️⃣ Parse HTML:
Uses `BeautifulSoup` to parse the HTML content and extract the movie titles and their ranks.

3️⃣ Save to File:
Writes the extracted movie data to a text file named `best_movies.txt`.

## Setup and Usage

1. Clone this repository to your local machine.

2. Ensure you have the following Python packages installed:

    ```bash
    pip install requests beautifulsoup4
   ```

3. Execute the Python script to scrape the movie data and save it to a text file:

   ```bash
   python main.py
   ```

## *Enjoy the* 🧼 *!*