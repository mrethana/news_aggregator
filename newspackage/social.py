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

def random_difficulties(length_of_df):
    difficulties = []
    for i in list(range(0,length_of_df)):
        difficulties.append(random.choice(['Easy','Medium','Hard']))
    return difficulties

def tokenize_text(words):
    tokenizer = RegexpTokenizer('[A-Za-z]\w+')
    all_tokens = tokenizer.tokenize(words)
    case_insensitive = [token.lower() for token in all_tokens]
    bigrams = list(ngrams(case_insensitive,2))
    joined = [' '.join(gram) for gram in bigrams]
    trigrams = list(ngrams(case_insensitive,3))
    tri_joined = [' '.join(gram) for gram in trigrams]
    case_insensitive.extend(joined)
    case_insensitive.extend(tri_joined)
    return set(case_insensitive)

def clean_tweets(data, categories):
    topics = []
    topics2 = []
    topics3 = []
    topics4 = []
    topics5 = []
    for tweet in data:
        categories_dict = {1:'null',2:'null',3:'null',4:'null',5:'null'}
        words = tokenize_text(tweet.text)
        intersection = list(words.intersection(categories))
        if len(intersection) > 0:
            for i in list(range(0,len(intersection))):
                categories_dict[i+1] = intersection[i]
        else:
            categories_dict[1] = 'general'
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
nyt_fb_post = ['https://www.facebook.com/WellNYT/posts/2030812243705795', 'https://www.facebook.com/WellNYT/posts/2027922970661389',
              'https://www.facebook.com/WellNYT/posts/2027920193995000','https://www.facebook.com/WellNYT/posts/2023650137755339',
              'https://www.facebook.com/WellNYT/posts/2022428551210831','https://www.facebook.com/WellNYT/posts/2022404617879891']

nyt_fb_vid = ['https://www.facebook.com/WellNYT/videos/vl.215269862225520/1148312565289105/?type=1','https://www.facebook.com/WellNYT/videos/vl.215269862225520/1146634572123571/?type=1',
         'https://www.facebook.com/WellNYT/videos/vl.215269862225520/1146398342147194/?type=1', 'https://www.facebook.com/WellNYT/videos/1437656589688033/'
         ,'https://www.facebook.com/WellNYT/videos/1408624012591291/','https://www.facebook.com/WellNYT/videos/1390021831118176/','https://www.facebook.com/WellNYT/videos/1363150167138676/',
         'https://www.facebook.com/WellNYT/videos/1362877763832583/']

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


categories = ['vegan','keto','vegetarian','paleo']

def create_sample_fb(list_urls, categories_list, medium_type):
    df = pd.DataFrame()
    df['web_url'] = list_urls
    df['image_url'] = list_urls
    df['description'] = 'Facebook Dummy Data'
    df['title'] = 'Facebook Dummy Data'
    df['date'] = '2018-12-26'
    df['medium'] = medium_type
    df['source'] = 'NYT Health'
    df['source_id'] = 'Facebook'
    df['formality'] = 'Informal'
    df['difficulty'] = 'Medium'
    length = len(df.web_url)
    df['length'] = random_length(length)
    df['param'] = random_cat(categories_list,length)
    return df

#INSTAGRAM

insta_post = ['https://www.instagram.com/p/Br2LWE1hHOc/','https://www.instagram.com/p/Br2LHsDB4rL/',
                 'https://www.instagram.com/p/Br2K-V8heFw/','https://www.instagram.com/p/Br1R6cjBI5j/',
                 'https://www.instagram.com/p/Br1RjfphbWn/','https://www.instagram.com/p/Br1RYYthKBq/',
                 'https://www.instagram.com/p/Bruqo-ihpaH/','https://www.instagram.com/p/BruqhH9BlJ0/',
                 'https://www.instagram.com/p/Brrp-7PBqlf/','https://www.instagram.com/p/BrrpzXIBbgC/','https://www.instagram.com/p/Brmjo72ByfA/',
                 'https://www.instagram.com/p/Brmjeg4huS_/','https://www.instagram.com/p/BrmjRICBXVk/','https://www.instagram.com/p/BrmhYKiBli5/']

def create_sample_insta(list_urls, categories_list):
    df = pd.DataFrame()
    df['web_url'] = list_urls
    df['image_url'] = list_urls
    df['description'] = 'Instagram Dummy Data'
    df['title'] = 'Instagram Dummy Data'
    df['date'] = '2018-12-26'
    df['source'] = 'Daily Health Tips'
    df['source_id'] = 'Instagram'
    df['formality'] = 'Informal'
    df['difficulty'] = 'Easy'
    df['medium'] = 'video'
    length = len(df.web_url)
    df['length'] = random_length(length)
    df['param'] = random_cat(categories_list,length)
    return df
