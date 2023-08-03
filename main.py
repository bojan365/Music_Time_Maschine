from bs4 import BeautifulSoup
import requests

BILLBOARD_HOT_TOP_100_URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? "
             "type the date in this format 'YYYY-MM-DD': ")
response = requests.get(url=BILLBOARD_HOT_TOP_100_URL + date)
html_page = response.text
soup = BeautifulSoup(html_page, "html.parser")
music_list = soup.select(selector='li #title-of-a-story')
music_titles = [_.getText().strip() for _ in music_list]
print(music_titles)
print(soup.select("title"))
