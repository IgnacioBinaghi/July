from notion_client import Client
import requests
import json
import os
from notion_database.page import Page
import re
from datetime import datetime, timezone

notion = Client(auth="secret_K1L1ySh3uTqQpRtWfT3S1LTm7pz9euMEMg5WixK3j1Q")


def create_item(databaseId, content):
    key = os.environ.get("secret_K1L1ySh3uTqQpRtWfT3S1LTm7pz9euMEMg5WixK3j1Q")
    headers = {'Authorization': f"Bearer secret_K1L1ySh3uTqQpRtWfT3S1LTm7pz9euMEMg5WixK3j1Q", 
           'Content-Type': 'application/json', 
           'Notion-Version': '2022-06-28'}
    create_page_body = {
        "parent": { "database_id": databaseId },
        "properties": {
            "\ufeffName": {
                "title": [{ 
                    "type": "text", 
                    "text": { "content": content[0] } 
                }]
            },
            "Status": {
                "select": { "name": 'For Review' }
            },
            "Email": {
                "email": content[1]
            },
            "Size": {
                "rich_text": [{ 
                    "type": "text", 
                    "text": { "content": content[2] } 
                }]
            },
            "Reference": {
                "url": 'https://www.tiktok.com/@'+content[0]
            },
            "Links": {
                "url": content[3]
            }
        }
    }
    create_response = requests.post(
    "https://api.notion.com/v1/pages", 
    json=create_page_body, headers=headers)



def accept_creator(database_id, page_id):
    updated_page = notion.pages.update(
    page_id,
    properties={
        "Status": {
            "select": {
                "name": "Accepted"
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




