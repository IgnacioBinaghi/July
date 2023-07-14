from apify_client import ApifyClient
import json
import re
from get import *
from getNotion import *
from bs4 import BeautifulSoup
import requests


client = ApifyClient('apify_api_CT8OLmgJ5LgycyhOYOUwj4aybbIAo90FPvSo')



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

def get_users_returned(hashtags, keywords):
    users = []
    usernames = []
    accepted = []
    # Prepare the actor input
    run_input = {
        "hashtags": hashtags,
        "resultsPerPage": 5000,
        "proxyConfiguration": { "useApifyProxy": True },
    }

    # Run the actor and wait for it to finish
    run = client.actor("clockworks/tiktok-scraper").call(run_input=run_input)

    # Fetch and print actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():

        username = item['authorMeta']['name']
        if username not in usernames:
            usernames.append(username)
        else:
            pass

    print('Creators Retrieval Successful')

    usernames = list(set(usernames))

    stats = get_stats(usernames)


    for item in stats:
        users.append([item[0], find_email(item[2]), item[1], item[3], item[2]])


    for i in users:
        for u in keywords:
            if u in i[4]:
                accepted.append(i)

    return accepted



def get_users(hashtags, keywords):
    count = 0
    start_time = time.time()
    accepted = []
    users = get_users_returned(hashtags, keywords)
    for i in users:
        progress_bar(count, len(users), start_time)


        if i[1] != None:
            accepted.append(i)
        elif i[1] == None:
            if get_url_email(i[3]) != None:
                i[1] = get_url_email(i[3])
                accepted.append(i)
        else:
            pass

        count+=1

    return accepted


