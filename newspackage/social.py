import tweepy
from apikeys import *
import pandas as pd
import json
import requests
import datetime
from datetime import date
import re
from info import *

auth = tweepy.OAuthHandler(twitter_1, twitter_2)
auth.set_access_token(twitter_3, twitter_4)
api = tweepy.API(auth)

#clean response from twitter

def clean_tweets(data, categories):
    topics = []
    for tweet in data:
        try:
            hashtag = tweet.entities['hashtags'][0]['text']
            tags = list(pd.DataFrame(tweet.entities['hashtags']).text)
            intersect = list(set(tags).intersection(categories))
            if len(intersect) > 0:
                hashtag = intersect[0]
            else:
                hashtag = hashtag
        except IndexError:
            words = set(re.sub("[^\w]", " ",  tweet.text).split())
            int2 = list(words.intersection(categories))
            if len(int2) > 0:
                hashtag = int2[0]
            else:
                hashtag = 'general'
        topics.append(hashtag)
    tweets = [{'title':tweet.id, 'date':tweet.created_at.date().strftime('%Y-%m-%d'),
       'description': tweet.text, 'source':tweet.user.screen_name,'source_id':tweet.user.id_str,
       'formality': 'Informal'
       ,'length': 1,'medium':'text'} for tweet in data]
    tweets = pd.DataFrame(tweets)
    tweets['param'] = topics
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
