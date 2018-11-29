import requests
import json
import feedparser
import pandas as pd
import re
import time


def feed_urls(search_words, media_value='podcast', entity_value='podcast'):
#     Args:
#         search_words: The URL-encoded text string to be searched for
#         media_value: {movie, podcast, music, musicVideo, audiobook,
#                     shortFilm, tvShow, software, ebook, all} optional
#                     An optional variable, which indicates the media type to be searched for.
#         entity_value: Optional

    payload = {'term': search_words, 'media': media_value, 'entity' : entity_value}
    itunes_request = requests.get('https://itunes.apple.com/search', params=payload)
    itunes_result_json = itunes_request.json()
    result_count = itunes_result_json["resultCount"]
    if result_count > 0:
        feed_url = itunes_result_json["results"][0]['feedUrl']
    else:
        feed_url = "None"
    return feed_url

def fix_podcast_length(time):
    hours = int(time[0:2]) * 60
    minutes = int(time[4:5])
    length = hours + minutes
    return length

def df_podcast_episodes(feed_url):
    print(feed_url)
    if(len(feed_url) > 0):
        feed = feedparser.parse(feed_url)
        episodes = []
        for episode in feed.entries:
            info = dict()
            info['title'] = episode['title'] if 'title' in episode else ''
            info['description']= episode['summary'] if 'summary' in episode else ''
            info['length']= fix_podcast_length(episode['itunes_duration']) if 'itunes_duration' in episode else 1
            info['date']= pd.to_datetime(episode['published']).date().strftime('%Y-%m-%d') if 'published' in episode else ''
            info['medium'] = 'audio'
            info['formality'] = 'Intermediate'
            info['source'] = feed['feed']['title'] if 'title' in feed['feed'] else ''
            info['source_id'] = feed['feed']['title_detail']['base'] if 'title_detail' in feed['feed'] else ''
            try:
                info['web_url'] = episode['links'][0]['href'] if 'links' in episode else ''
            except:
                info['web_url'] = feed['feed']['title_detail']['base'] if 'title_detail' in feed['feed'] else ''
            info['image_url'] = feed['feed']['image']['href'] if 'image' in feed['feed'] else ''
            episodes.append(info)
        df = pd.DataFrame(episodes)
        return df
    else:
        print("No response!")

def add_category_to_audio(df, categories):
    all_params = []
    for index, row in df.iterrows():
        try:
            words = set(re.sub("[^\w]", " ",  row.description).split())
            intersect = list(words.intersection(categories))
            if len(intersect) > 0:
                category = intersect[0]
            else:
                category = 'general'
        except:
            category = 'general'
        all_params.append(category)
    df['param'] = all_params
    return df

def call_podcast_api(categories, podcasts):
    empty = pd.DataFrame()
    for podcast in podcasts:
        if podcast == 'None':
            pass
        else:
            try:
                url = feed_urls(podcast)
                df = df_podcast_episodes(url)
                df = add_category_to_audio(df, categories)
                empty = empty.append(df, sort=True)
                print('SUCCESS!')
                time.sleep(2)
            except:
                print('EXCEPTION')
                time.sleep(2)
    return empty

#######EBOOKS

def clean_ebook_date(df):
    dates = []
    for index, row in df.iterrows():
        date = pd.to_datetime(row.date).date().strftime('%Y-%m-%d')
        dates.append(date)
    df['date'] = dates
    return df


def ebook_search(search_word, media_value='ebook', entity_value='ebook'):
    payload = {'term': search_word, 'media': media_value, 'entity' : entity_value}
    itunes_request = requests.get('https://itunes.apple.com/search', params=payload)
    itunes_result_json = itunes_request.json()
    result_count = itunes_result_json["resultCount"]
    if result_count > 0:
        df = pd.DataFrame(itunes_result_json['results'])
        #NOTE LENGTH IS ACTUALLY THE PRICE BUT USE SAME LABEL FOR CONSISTENCY
        df = df.rename(index = str, columns= {'artistName': 'source','trackViewUrl':'web_url',
                                        'artworkUrl100':'image_url','price': 'length','releaseDate':'date','trackName':'title'})
        df['source_id'] = 'Itunes Ebook'
        df['formality'] = 'Formal'
        df['medium'] = 'text'
        df['param'] = search_word
        df = df.fillna(1)
        return clean_ebook_date(df)
    else:
        print('No Results!')
        return 'Empty'

def call_ebook_api(categories):
    empty = pd.DataFrame()
    for category in categories:
        df = ebook_search(category)
        if type(df) != str:
            empty = empty.append(df, sort=True)
            time.sleep(2)
            print('Added '+category)
        else:
            time.sleep(2)
    return empty


###### MOVIE SEARCH

def add_category_to_movie(df, categories):
    all_params = []
    for index, row in df.iterrows():
        try:
            words = set(re.sub("[^\w]", " ",  row.description).split())
            intersect = list(words.intersection(categories))
            if len(intersect) > 0:
                category = intersect[0]
            else:
                category = 'general'
        except:
            category = 'general'
        all_params.append(category)
    df['param'] = all_params
    return df

def movie_search(search_word,categories, media_value='movie', entity_value='movie'):
    payload = {'term': search_word, 'media': media_value, 'entity' : entity_value}
    itunes_request = requests.get('https://itunes.apple.com/search', params=payload)
    itunes_result_json = itunes_request.json()
    result_count = itunes_result_json["resultCount"]
    if result_count > 0:
        df = pd.DataFrame(itunes_result_json['results'])
        df = df.rename(index = str, columns= {'artistName': 'source','trackViewUrl':'web_url',
                                        'artworkUrl100':'image_url','trackTimeMillis': 'length'
                                              ,'releaseDate':'date','trackName':'title', 'longDescription':'description'})
        df['source_id'] = 'Itunes Movie'
        df['formality'] = 'Formal'
        df['medium'] = 'video'
        df['length'] = round(df['length'] / 60000)
        df = df.fillna(1)
        df = clean_ebook_date(df)
        return add_category_to_movie(df,categories)
    else:
        print('No Results!')
        return 'Empty'

def call_movie_api(movies, categories):
    empty = pd.DataFrame()
    for movie in movies:
        try:
            df = movie_search(movie, categories)
            if type(df) != str:
                empty = empty.append(df, sort=True)
                time.sleep(5)
                print('Added '+movie)
            else:
                time.sleep(5)
        except:
            print(movie + ' EXCEPTION')
    return empty

def audiobook_search(search_word, media_value='audiobook', entity_value='audiobook'):
    payload = {'term': search_word, 'media': media_value, 'entity' : entity_value}
    itunes_request = requests.get('https://itunes.apple.com/search', params=payload)
    itunes_result_json = itunes_request.json()
    result_count = itunes_result_json["resultCount"]
    if result_count > 0:
        df = pd.DataFrame(itunes_result_json['results'])
        #NOTE LENGTH IS ACTUALLY THE PRICE BUT USE SAME LABEL FOR CONSISTENCY
        df = df.rename(index = str, columns= {'artistName': 'source','collectionViewUrl':'web_url',
                                        'artworkUrl100':'image_url','price': 'length','releaseDate':'date','collectionName':'title'})
        df['source_id'] = 'Itunes Audiobook'
        df['formality'] = 'Formal'
        df['medium'] = 'audio'
        df['param'] = search_word
        df = df.fillna(1)
        return clean_ebook_date(df)
    else:
        print('No Results!')
        return 'Empty'

def call_audiobook_api(categories):
    empty = pd.DataFrame()
    for category in categories:
        df = audiobook_search(category)
        if type(df) != str:
            empty = empty.append(df, sort=True)
            time.sleep(2)
            print('Added '+category)
        else:
            pass
    return empty
