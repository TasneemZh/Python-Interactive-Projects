# Top Songs Spotify Playlist

Welcome to the Top Songs Spotify Playlist! This project allows you to scrape the Billboard Hot 100 songs for a specific date and create a private playlist on Spotify with those songs.

## Project Overview

This project consists of two main parts:

- Hot Songs Scraper:
Scrapes the Billboard Hot 100 songs for a given date.
- Spotify Playlist Creator:
Uses the scraped songs to create a private Spotify playlist.

## Setup and Usage

1. Prerequisites
   - Python 3.x
   - Spotify Developer Account
   - Spotify App with client credentials]()

2. Installation
   - Clone the repository.
   - Install the required packages:
       ```bash
       pip install requests beautifulsoup4 spotipy python-dotenv
       ```
   - Create a .env file in the project root with your Spotify credentials:
       ```makefile
       SPOTIFY_CLIENT_ID=your_spotify_client_id
       SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
       SPOTIFY_REDIRECT_URL=your_spotify_redirect_url
       ```

## Running the Project

1. Execute the main.py script to start the process:
    ```bash
    python main.py
    ```

2. When prompted, enter the year and month you want to travel to for the Billboard Hot 100 songs.

3. The script will process the songs, create a Spotify playlist, and add the songs to the playlist. Follow the console outputs for progress updates.

## *Enjoy the* 🎼 *!*