import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_top_songs():
    user_year = input("What year would you like to travel to? ")
    user_month = input("What month would you like to travel to? ")

    now = datetime.now()
    if not user_year:
        user_year = now.year
    if not user_month:
        user_month = now.month

    response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_year}-{user_month}-01/")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    songs = soup.find_all(name="h3", class_="a-font-primary-bold-s")

    song_titles = [song.text.strip() for song in songs[2:]]

    return {"song_titles": song_titles, "date": f"{user_year}-{user_month}-01"}
