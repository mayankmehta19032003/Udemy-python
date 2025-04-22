import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h3", class_="title")

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles:
        movie_title = title.get_text()
        file.write(f"{movie_title}\n")
        print(title)
    


