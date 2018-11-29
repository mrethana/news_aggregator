from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import pprint
import pafy
import warnings
warnings.filterwarnings("ignore")
from apikeys import *
from info import *


DEVELOPER_KEY = youtube_key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def clean_youtube_time(string):
    if 'H' in string:
        minutes = int(string[string.find('H')+1:string.find('M')])
        hours = int(string[string.find('T')+1:string.find('H')]) * 60
        time = minutes + hours
    else:
        if 'M' in string:
            time = int(string[string.find('T')+1:string.find('M')])
        else:
            time = 1
    return time

def youtube_search(q, max_results=50,order="date", token=None, location=None, location_radius=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet", # Part signifies the different types of data you want
    maxResults=max_results,
    location=location,
    locationRadius=location_radius).execute()

    all_dicts = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":

            title = (search_result['snippet']['title'])

            videoId = (search_result['id']['videoId'])

            response = youtube.videos().list(
            part='statistics, snippet, contentDetails',
            id=search_result['id']['videoId']).execute()

            channelId = (response['items'][0]['snippet']['channelId'])
            channelTitle = (response['items'][0]['snippet']['channelTitle'])
            categoryId = (response['items'][0]['snippet']['categoryId'])
            favoriteCount = (response['items'][0]['statistics']['favoriteCount'])
            viewCount = (response['items'][0]['statistics']['viewCount'])
            date = pd.to_datetime((response['items'][0]['snippet']['publishedAt'])).date().strftime('%Y-%m-%d')
            description = response['items'][0]['snippet']['localized']['description']
            url = 'https://www.youtube.com/watch?v='+videoId
            image_url = response['items'][0]['snippet']['thumbnails']['default']['url']
            length = clean_youtube_time(response['items'][0]['contentDetails']['duration'])

        if 'commentCount' in response['items'][0]['statistics'].keys():
            commentCount = (response['items'][0]['statistics']['commentCount'])
        else:
            commentCount = []

        if 'tags' in response['items'][0]['snippet'].keys():
            tags = (response['items'][0]['snippet']['tags'])
        else:
            tags = []

        youtube_dict = {'tags':tags,'source_id': channelId,'source': channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':viewCount,'commentCount':commentCount,'favoriteCount':favoriteCount,
                        'formality':'Intermediate', 'medium':'video','date':date, 'description': description, 'web_url':url, 'image_url':image_url, 'length':length}
        all_dicts.append(youtube_dict)
    return pd.DataFrame(all_dicts)

def add_category(df, categories):
    # cats = ['keto','ketogenic','paleo','paleolithic','vegan','vegetarian']
    all_params = []
    for index, row in df.iterrows():
        try:
            intersect = list(set(row.tags).intersection(categories))
            if len(intersect) > 0:
                category = intersect[0]
            else:
                category = row.tags[0]
        except:
            category = 'general'
        all_params.append(category)
    df['param'] = all_params
    return df

def youtube_api_call(list_accounts, categories):
    empty_df = pd.DataFrame()
    errors = []
    for account in list_accounts:
        try:
            df = youtube_search(account)
            df = add_category(df, categories)
            empty_df = empty_df.append(df, sort=True)
            print(account)
        except:
            print(account + " EXCEPTION!!!!")
    return empty_df
