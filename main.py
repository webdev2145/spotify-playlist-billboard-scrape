import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from credentials import *

#TODO 1: Scrape billboard top 100 website
URL = 'https://www.billboard.com/charts/hot-100/'
date = '2020-12-26'
date = input("Enter date to use for creating playlist (YYYY-MM-DD): ")

response = requests.get(url=f'{URL}{date}')

songs_soup = BeautifulSoup(response.text, "html.parser")
# print(response.text)

songs_data = songs_soup.find_all(name='span', class_="chart-element__information__song")

# songs_data = songs_soup.findAll(name='span', {'class': ["chart-element__information__song", "text--truncate", "color--primary"]})

for song in songs_data:
    print(song.get_text())

#TODO 2: Create spotify playlist