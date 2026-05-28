from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.billboard.com/charts/pakistan-songs-hotw/"
def get_top_songs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup.prettify())
    songs = []
    raw_songs = soup.select("li h3[id='title-of-a-story']")

    for song in raw_songs:
        songs.append(song.get_text(strip=True))

    return songs
