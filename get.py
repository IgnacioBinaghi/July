import requests
from bs4 import BeautifulSoup
import sys
import time


def get_info(username):

    users = []
    count = 0
    start_time = time.time()


    url = 'https://www.tiktok.com/@'+username

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id = 'main-content-others_homepage')

    try:
        html = results.find_all(attrs={'class': 'tiktok-1zpj2q-ImgAvatar e1e9er4e1'})
        soup = BeautifulSoup(str(html), 'html.parser')
        img = soup.find('img')
        pfp = img['src']
    except:
        pfp = ''

    try:
        html = results.find_all(attrs={'class': 'tiktok-vdfu13-H2ShareDesc'})

        soup = BeautifulSoup(str(html), 'html.parser')

        text = soup.get_text()

        bio = text[1:-1]
    except:
        bio = ''

    try:
        html = results.find_all(attrs={'class': 'tiktok-rxe1eo-DivNumber e1457k4r1'})
        soup = BeautifulSoup(str(html), 'html.parser')
        followers = soup.find('strong', {'data-e2e': 'followers-count'}).text
    except:
        followers = ''
            
    try:
        html = results.find_all(attrs={'class': 'tiktok-847r2g-SpanLink eht0fek2'})
        soup = BeautifulSoup(str(html), 'html.parser')
        link = soup.find('span', {'class': 'tiktok-847r2g-SpanLink'}).text
    except:
        link = ''


    user = [username, pfp, followers, bio, link]


    return user