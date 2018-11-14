import tweepy
from apikeys import *
import pandas as pd
import json
import requests
import datetime
from datetime import date

auth = tweepy.OAuthHandler(twitter_1, twitter_2)
auth.set_access_token(twitter_3, twitter_4)
api = tweepy.API(auth)
#all twitter handles to scrape
twitter_handles = ['@ATPScience1', '@waitrose', '@MicrobiomeInst', '@veganrecipescom', '@cldiet', '@Onnit', '@vegsoc', '@VeganKosher', '@TheVeganSociety', '@vegan', '@Keto_Recipes_', '@the52diet', '@IFdiet', '@microbiome', '@metagenomics', '@microbiome_news', '@TheGutStuff', '@MyGutHealth', '@PaleoFX',
'@PaleoFoundation', '@ThePaleoDiet', '@PaleoComfort', '@cavemanketo', '@KetoFlu', '@TheKetoKitchen_', '@EatKetoWithMe', '@KetoConnect', '@KetoDietZone', '@Ketogenic', '@USDANutrition', '@FoodRev', '@CSPI', '@simplyrecipes', '@FoodNetwork', '@CookingChannel', '@tasty', '@nytfood', '@finecooking', '@mrcookingpanda'
, '@FODMAPeveryday', '@FODMAPLife', '@FodmappedInfo', '@thefodmapdoctor', '@SimplyGlutenFre', '@gfliving', '@sibotest', '@manjulaskitchen', '@VegTimes', '@CookingLight', '@mealprepwl', '@thehealthygut', '@VitalGutHealth', '@pureguthealth', '@PaleoForBegin', '@PaleoLeap', '@ThePaleoMom', '@paleomagazine', '@PaleoHacks', '@paleogrubs',
'@naturalgourmet', '@Low_Carb_Keto', '@NutritionTwins', '@mckelhill', '@WomensFitnessAu', '@WomensHealthMag', '@MensHealthMag', '@mjfit', '@thugkitchen', '@Leslie_Klenke', '@insidePN', '@ThisMamaCooks', '@EdibleWildFood', '@TheEarthDieter', '@HarvardHealth', '@EverydayHealth', '@DailyHealthTips']

#clean response from twitter
def clean_tweets(data):
    tweets = []
    for tweet in data:
        try:
            hashtag = tweet.entities['hashtags'][0]['text']
        except IndexError:
            hashtag = 'unknown'
        tweets = [{'title':tweet.id, 'date':tweet.created_at.date().strftime('%Y-%m-%d'),
           'description': tweet.text, 'source':tweet.user.screen_name,'source_id':tweet.user.id_str,
           'formality': 'Informal'
           ,'length': 1,'medium':'text', 'param':hashtag} for tweet in data]
    tweets = pd.DataFrame(tweets)
    return tweets
#call api
def twitter_api_call(list_handles):
    empty = pd.DataFrame()
    for handle in list_handles:
        user_tweets = pd.DataFrame(clean_tweets(api.user_timeline(handle)))
        empty = empty.append(user_tweets, sort=True)
        print(handle)
    empty.title = empty.title.astype('str')
    empty['web_url'] = 'https://twitter.com/'+empty.source+'/status/'+empty.title
    empty['image_url'] = empty['web_url']
    return empty
