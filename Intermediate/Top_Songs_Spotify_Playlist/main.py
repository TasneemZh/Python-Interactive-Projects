import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from top_songs_scraper import get_top_songs

load_dotenv(".env")

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

songs_data = get_top_songs()
songs = songs_data["song_titles"]
playlist_name = f"{songs_data["date"]} Billboard 100"

print("Processing...")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=os.environ.get("SPOTIFY_REDIRECT_URL"),
                                               scope="playlist-modify-private"))

spotify_user = sp.current_user()

print("Still processing...")

playlist_create = sp.user_playlist_create(user=spotify_user["id"], name=playlist_name,
                                          description="The first 100 hot songs!",
                                          public=False)

song_urls = []
for song in songs:
    search_result = sp.search(q=song, type='track', limit=1, offset=0)
    try:
        song_url = search_result["tracks"]["items"][0]["external_urls"]["spotify"]
        song_urls.append(song_url)
    except KeyError:
        pass

print("Almost Done...")

playlist_items = sp.playlist_add_items(playlist_id=playlist_create["id"], items=song_urls)

print("Completed!")
