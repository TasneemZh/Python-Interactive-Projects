import requests
from pathlib import Path
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

file_path = Path("best_movies.txt")
if file_path.exists():
    file_path.unlink()

for movie in movies[::-1]:
    movie_part1 = movie.text[:movie.text.index(' ')]
    movie_part2 = movie.text[movie.text.index(' ') + 1:]
    rank_txt = [int(s) for s in movie_part1 if s.isdigit()]
    rank = "".join(str(num) for num in rank_txt)
    print({"title": movie_part2, "rank": int(rank)})
    with open("best_movies.txt", mode="a") as file:
        file.write(f"{int(rank)} {movie_part2}\n")


