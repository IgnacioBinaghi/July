from notion_client import Client
import requests
import json
import os
from notion_database.page import Page



notion = Client(auth="secret_K1L1ySh3uTqQpRtWfT3S1LTm7pz9euMEMg5WixK3j1Q")

user_info = []



def read_database(database_id):
    user_info = []
    results = notion.databases.query(
        **{
            "database_id": database_id,
        }
    ).get("results")

    for row in results:
        val = []
        try:
            name = row['properties']['\ufeffName']['title'][0]['text']['content']
            val.append(name)
        except:
            name = ''
            val.append(name)

        try:
            status = row['properties']['Status']['select']['name']
            if status != 'For Review':
                continue
            val.append(status)
        except:
            status = ''
            val.append(status)


        try:
            status = row['properties']['Email']['email']
            val.append(status)
        except:
            status = ''
            val.append(status)

        try:
            size = row['properties']['Size']['rich_text'][0]['text']['content']
            val.append(size)
        except:
            size = ''
            val.append(size)

        try:
            socials = row['properties']['Reference']['url']
            val.append(socials)
        except:
            socials = ''
            val.append(socials)

        try:
            extra_info = row['properties']['Links']['url']
            val.append(extra_info)
        except:
            extra_info = ''
            val.append(extra_info)

        page_id = row['id']
        val.append(page_id)


        user_info.append(val)

    return user_info


def check_valid_username(username, db_id):
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

    if username.upper() in map(str.upper, usernames):
        return False

    return True




def update_item(databaseId, content, page_id):
    key = os.environ.get("secret_K1L1ySh3uTqQpRtWfT3S1LTm7pz9euMEMg5WixK3j1Q")
    headers = {'Authorization': f"Bearer secret_K1L1ySh3uTqQpRtWfT3S1LTm7pz9euMEMg5WixK3j1Q", 
           'Content-Type': 'application/json', 
           'Notion-Version': '2022-06-28'}
    search_params = {"filter": {"value": "page", "property": "object"}}
    search_response = requests.post(f'https://api.notion.com/v1/search', json=search_params, headers=headers)

    search_results = search_response.json()["results"]

    create_page_body = {
        "parent": { "page_id": page_id },
        "properties": {
            "title": {
          "title": [{ 
              "type": "text", 
              "text": { "content": 'Ready To Send' } }]
               }
        },
        "children": [
        {
             "object": "block",
              "type": "paragraph",
             "paragraph": {
            "rich_text": [{ 
              "type": "text", 
               "text": { 
                  "content": content}
                } 
            ]
          }
        }
      ]
    }

    create_response = requests.post(
    "https://api.notion.com/v1/pages", 
    json=create_page_body, headers=headers)

    updated_page = notion.pages.update(
    page_id,
    properties={
        "Status": {
            "select": {
                "name": "Ready To Send"
            }
        }
    }
)


def deny_creator(database_id, page_id):
    updated_page = notion.pages.update(
    page_id,
    properties={
        "Status": {
            "select": {
                "name": "Rejected"
            }
        }
    }
)











