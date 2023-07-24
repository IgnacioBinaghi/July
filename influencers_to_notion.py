from notion_client import Client
import requests
import json
import os
from notion_database.page import Page

notion = Client(auth="secret_K1L1ySh3uTqQpRtWfT3S1LTm7pz9euMEMg5WixK3j1Q")


def create_item(databaseId, name, email, size, link):
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
                    "text": { "content": name } 
                }]
            },
            "Status": {
                "select": { "name": 'New' }
            },
            "Email": {
                "email": email
            },
            "Size": {
                "rich_text": [{ 
                    "type": "text", 
                    "text": { "content": size } 
                }]
            },
            "Reference": {
                "url": 'https://www.tiktok.com/@'+name
            },
            "Links": {
                "url": link if link else None
            }
        }
    }
    create_response = requests.post(
    "https://api.notion.com/v1/pages", 
    json=create_page_body, headers=headers)