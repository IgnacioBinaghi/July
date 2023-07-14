from get_influencers import *
from influencers_to_notion import *
import os
import time

copilot_hashtags = ["#personalfinance", '#invest', '#finance', '#investingtips', '#businesstips', '#moneytips', '#investing']
copilot_keywords = ['Money', 'finance', 'invest', 'investing', 'financial', 'personal finance', 'trader', 'trading', 'financially', 'financial']
databass_hashtags = ['#producer','#musicproducer','#prodcommunity','#audioengineering','#sounddesign', '#musicproduction', '#productiontips']
databass_keywords = ['producer','music','audio','engineer','sound','design','musician', 'composer', 'production']
iago_hashtags = ['#learnjapanese', '#studyjapanese', '#japaneselearning', '#JapaneseLearner', '#日本語勉強', '#japaneselesson', '#japaneselanguage']
iago_keywords = ['certified','professor','teacher','learn','japanese learning','study','learning', 'tutor', 'tutoring', 'studying']
edge_hashtags = ['#ecommerce', '#reseller', '#resell', '#reselling', '#sneakers', '#kicks', '#onlinebusiness', '#amazonFBA', '#elevatebusiness', '#growyourbusiness', '#businessgrowth']
edge_keywords = ['reseller', 'sneakerhead', 'resell', 'ecommerce', 'invest', 'grow', 'sneaker', 'sneakers', 'investing', 'finance', 'online business', 'FBA', 'growth']
Tella_hashtags = ['#solopreneur', '#freelance', '#UXdesigner', '#productmanager', '#marketing', '#productivity', '#tech', '#UXdesign', '#contentcreator', '#technology']
Tella_keywords = ['solopreneur', 'freelancer', 'freelance', 'UX', 'tech', 'productivity', 'productive', 'marketer', 'product manager', 'creator', 'technology']
Abode_hashtags = ['#homeowner', '#homeownership', '#realestate', '#homedecor', '#homeownertips', '#homeorganization', '#propertyowner']
Abode_keywords = ['Real Estate', 'homeowner', 'property', 'home', 'homeownership', 'decor']


businesses = {
'iago': [iago_hashtags,iago_keywords],
 'Copilot': [copilot_hashtags,copilot_keywords],
  'Somethings': [[],[]],
   'playground': [[],[]],
    'Edge': [edge_hashtags,edge_keywords],
     'Databass':[databass_hashtags,databass_keywords],
      'Tella': [Tella_hashtags,Tella_keywords],
      'Abode': [Abode_hashtags,Abode_keywords]
      }


def get_businesses():
    return businesses


def main(db, business):

    time.sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')

    print('Searching For Creators...\n\n')

    users = get_users(businesses[business][0], businesses[business][1])
    print(len(users))

    print('\n\nAdding Creators to Notion...')
    for i in users:
        if check_valid_username(i[0], db):
            create_item(db, i)


