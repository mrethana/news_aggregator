from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import pprint
from apikeys import *


DEVELOPER_KEY = youtube_key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

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
            part='statistics, snippet',
            id=search_result['id']['videoId']).execute()

            channelId = (response['items'][0]['snippet']['channelId'])
            channelTitle = (response['items'][0]['snippet']['channelTitle'])
            categoryId = (response['items'][0]['snippet']['categoryId'])
            favoriteCount = (response['items'][0]['statistics']['favoriteCount'])
            viewCount = (response['items'][0]['statistics']['viewCount'])
            likeCount = (response['items'][0]['statistics']['likeCount'])
            dislikeCount = (response['items'][0]['statistics']['dislikeCount'])

        if 'commentCount' in response['items'][0]['statistics'].keys():
            commentCount = (response['items'][0]['statistics']['commentCount'])
        else:
            commentCount = []

        if 'tags' in response['items'][0]['snippet'].keys():
            tags = (response['items'][0]['snippet']['tags'])
        else:
            tags = []

        youtube_dict = {'tags':tags,'channelId': channelId,'channelTitle': channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount}
        all_dicts.append(youtube_dict)
    return pd.DataFrame(all_dicts)
