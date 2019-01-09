import tweepy
from apikeys import *
import pandas as pd
import json
import requests
import datetime
from datetime import date
import re
from info import *
import random
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
from nltk.tokenize import RegexpTokenizer

auth = tweepy.OAuthHandler(twitter_1, twitter_2)
auth.set_access_token(twitter_3, twitter_4)
api = tweepy.API(auth)

#clean response from twitter


def clean_tweets(data, categories):
    topics = []
    topics2 = []
    topics3 = []
    topics4 = []
    topics5 = []
    for tweet in data:
        categories_dict = find_categories(tweet.text, categories)
        topics.append(categories_dict[1])
        topics2.append(categories_dict[2])
        topics3.append(categories_dict[3])
        topics4.append(categories_dict[4])
        topics5.append(categories_dict[5])
    tweets = [{'title':tweet.id, 'date':tweet.created_at.date().strftime('%Y-%m-%d'),
       'description': tweet.text, 'source':tweet.user.screen_name,'source_id':'Twitter',
       'formality': 'Informal',
       'length': 1,'medium':'text'} for tweet in data]
    tweets = pd.DataFrame(tweets)
    tweets['param_1'] = topics
    tweets['param_2'] = topics2
    tweets['param_3'] = topics3
    tweets['param_4'] = topics4
    tweets['param_5'] = topics5
    tweets['difficulty'] = random_difficulties(len(tweets['param_1']))
    return tweets



#CALL API
def twitter_api_call(list_handles, categories):
    empty = pd.DataFrame()
    for handle in list_handles:
        user_tweets = pd.DataFrame(clean_tweets(api.user_timeline(handle), categories))
        empty = empty.append(user_tweets, sort=True)
        print(handle)
    empty.title = empty.title.astype('str')
    empty['web_url'] = 'https://twitter.com/'+empty.source+'/status/'+empty.title
    empty['image_url'] = empty['web_url']
    return empty

#FACEBOOK
nyt_fb_post = [('https://www.facebook.com/WellNYT/posts/2030812243705795','NYT Health','text'),
('https://www.facebook.com/WellNYT/posts/2027922970661389','NYT Health','text'),
              ('https://www.facebook.com/WellNYT/posts/2027920193995000','NYT Health','text'),
              ('https://www.facebook.com/WellNYT/posts/2023650137755339','NYT Health','text'),
              ('https://www.facebook.com/WellNYT/posts/2022428551210831','NYT Health','text'),
              ('https://www.facebook.com/WellNYT/posts/2022404617879891','NYT Health','text')]

nyt_fb_vid = [('https://www.facebook.com/WellNYT/videos/vl.215269862225520/1148312565289105/?type=1','NYT Health','video')
,('https://www.facebook.com/WellNYT/videos/vl.215269862225520/1146634572123571/?type=1', 'NYT Health','video'),
         ('https://www.facebook.com/WellNYT/videos/vl.215269862225520/1146398342147194/?type=1','NYT Health','video')
         , ('https://www.facebook.com/WellNYT/videos/1437656589688033/','NYT Health','video')
         ,('https://www.facebook.com/WellNYT/videos/1408624012591291/', 'NYT Health','video'),
         ('https://www.facebook.com/WellNYT/videos/1390021831118176/','NYT Health','video'),
         ('https://www.facebook.com/WellNYT/videos/1363150167138676/','NYT Health','video'),
         ('https://www.facebook.com/WellNYT/videos/1362877763832583/','NYT Health','video'),
         ('https://www.facebook.com/WellNYT/videos/1362877763832583/','NYT Health','video')]

def random_cat(list_categories, length):
    cats = []
    for i in list(range(0,length)):
        cats.append(random.choice(list_categories))
    return cats

def random_length(length):
    lengths = []
    for i in list(range(0,length)):
        lengths.append(random.randint(0, 15))
    return lengths



def create_sample_fb(list_tuples, categories_list):
    diets = ['vegan','keto','vegetarian','paleo']
    df = pd.DataFrame()
    df['description'] = 'Facebook Dummy Data'
    df['title'] = 'Facebook Dummy Data'
    df['date'] = '2018-12-26'
    # df['medium'] = medium_type
    # df['source'] = 'NYT Health'
    df['source_id'] = 'Facebook'
    df['formality'] = 'Informal'
    length = len(df.title)
    df['difficulty'] = random_difficulties(length)
    df['length'] = random_length(length)
    df['param_1'] = random_cat(diets,length)
    df['param_2'] = random_cat(categories_list,length)
    df['param_3'] = random_cat(categories_list,length)
    df['param_4'] = random_cat(categories_list,length)
    df['param_5'] = random_cat(categories_list,length)
    urls = []
    images = []
    sources = []
    mediums = []
    for tuple in list_tuples:
        urls.append(tuple[0])
        images.append(tuple[0])
        sources.append(tuple[1])
        mediums.append(tuple[2])
    df['source'] = sources
    df['web_url'] = urls
    df['image_url'] = images
    df['medium'] = mediums
    return df

#INSTAGRAM

insta_post = [('https://www.instagram.com/p/Br2LWE1hHOc/','Daily Health Tips')
                ,('https://www.instagram.com/p/Br2LHsDB4rL/','Daily Health Tips'),
                 ('https://www.instagram.com/p/Br2K-V8heFw/','Daily Health Tips'),
                 ('https://www.instagram.com/p/Br1R6cjBI5j/','Daily Health Tips'),
                 ('https://www.instagram.com/p/Br1RjfphbWn/','Daily Health Tips'),
                 ('https://www.instagram.com/p/Br1RYYthKBq/','Daily Health Tips'),
                 ('https://www.instagram.com/p/Bruqo-ihpaH/','Daily Health Tips'),
                 ('https://www.instagram.com/p/BruqhH9BlJ0/','Daily Health Tips'),
                 ('https://www.instagram.com/p/Brrp-7PBqlf/','Daily Health Tips'),
                 ('https://www.instagram.com/p/BrrpzXIBbgC/','Daily Health Tips'),
                 ('https://www.instagram.com/p/Brmjo72ByfA/','Daily Health Tips'),
                 ('https://www.instagram.com/p/Brmjeg4huS_/','Daily Health Tips'),
                 ('https://www.instagram.com/p/BrmjRICBXVk/','Daily Health Tips'),
                 ('https://www.instagram.com/p/BrmhYKiBli5/','Daily Health Tips')]

def create_sample_insta(list_tuples, categories_list):
    diets = ['vegan','keto','vegetarian','paleo']
    df = pd.DataFrame()
    # df['web_url'] = list_urls
    # df['image_url'] = list_urls
    df['description'] = 'Instagram Dummy Data'
    df['title'] = 'Instagram Dummy Data'
    df['date'] = '2018-12-26'
    # df['source'] = 'Daily Health Tips'
    df['source_id'] = 'Instagram'
    df['formality'] = 'Informal'
    df['medium'] = 'video'
    length = len(df.title)
    df['difficulty'] = random_difficulties(length)
    df['length'] = random_length(length)
    df['param_1'] = random_cat(diets,length)
    df['param_2'] = random_cat(categories_list,length)
    df['param_3'] = random_cat(categories_list,length)
    df['param_4'] = random_cat(categories_list,length)
    df['param_5'] = random_cat(categories_list,length)
    urls = []
    images = []
    sources = []
    for tuple in list_tuples:
        urls.append(tuple[0])
        images.append(tuple[0])
        sources.append(tuple[1])
    df['source'] = sources
    df['web_url'] = urls
    df['image_url'] = images
    return df
