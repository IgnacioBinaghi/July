from notion_client import Client
import requests
import json
import os
from notion_database.page import Page



notion = Client(auth="secret_K1L1ySh3uTqQpRtWfT3S1LTm7pz9euMEMg5WixK3j1Q")

user_info = []


def get_usernames(db_id):
    usernames = []
    results = notion.databases.query(
        **{
            "database_id": db_id,
        }
    ).get("results")

    for row in results:
        try:
            name = row['properties']['\ufeffName']['title'][0]['text']['content']
            usernames.append(name)
        except:
            name = ''
            usernames.append(name)

    return usernames











