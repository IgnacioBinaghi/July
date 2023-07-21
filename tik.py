from tiktokapipy.api import TikTokAPI
from get import *
import re
from bs4 import BeautifulSoup
import requests
from getNotion import *


# https://tiktokpy.readthedocs.io/en/latest/index.html


def find_email(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    result = re.search(pattern, text)
    if result:
        return result.group()
    else:
        return None

def get_url_email(url):
    try:
        page = requests.get('http://'+url)
    except:
        return None

    soup = BeautifulSoup(page.content, 'html.parser')

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    result = re.search(pattern, str(soup))
    if result:
        return result.group()
    else:
        return None



creators = []
def find_creators(hashtags, creators, keywords, num_creators):
    total = 0
    num_creators = int(num_creators) // len(hashtags)
    with TikTokAPI() as api:
        for i in hashtags:
            count = 0
            try:
                challenge = api.challenge(i)
                for video in challenge.videos:
                    if int(num_creators) == int(count):
                        break
                    creator = str(video.author)[11:-1]
                    if (creator not in [sublist[0] for sublist in creators]) and (creator not in get_usernames('daf8b9db57984a1c9ade779c345f28d3')):
                        res = get_info(creator)
                        email = find_email(str(res[3]))
                        if email:
                            res.append(email)
                        else:
                            res.append(get_url_email(str(res[4])))
                        #for u in keywords:
                            #if u in res[2]:
                        creators.append(res)
                        print('Creator Found')
                        count+=1
            except Exception as e:
                print(e)
                continue
    return creators









