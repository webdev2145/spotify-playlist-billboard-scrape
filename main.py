import requests
from bs4 import BeautifulSoup

#TODO 1: Scrape billboard top 100 website
URL = 'https://www.billboard.com/charts/hot-100/'

date = input("Enter date to use for creating playlist (YYYY-MM-DD): ")

response = requests.get(url=f'{URL}/data')

print(response.text)


#TODO 2: Create spotify playlist