import requests
import re
import numpy as np
import time
from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
import datetime
from datetime import date
from apikeys import *
from info import *

#dates to use for API call
today = int(str(date.today()).replace('-',''))
last_week = int(str(date.today() - datetime.timedelta(days = 14)).replace('-',''))

#NEW YORK TIMES
#clean the response from NYT API
def NYT_title_clean(df):
    titles = []
    for index, row in df.iterrows():
        title = row.headline['main']
        titles.append(title)
    df['title'] = titles
    return df

def NYT_dropped_rows(df):
    df.pub_date = pd.to_datetime(df.pub_date).dt.date
    df.word_count = round(df.word_count / 150)
    df.document_type = 'text'
    df['formality'] = 'Intermediate'
    df['difficulty'] = random_difficulties(len(df['formality']))
    return df


def NYT_dataframe_clean(df):
    dataframe = NYT_title_clean(df)
    dataframe = NYT_dropped_rows(dataframe)
    return dataframe

# def NYT_api_call_section_based(section, source, page, start, end, key):
#     url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=section_name:({section_name})&page={page}&source:({source})&begin_date={start}&end_date={end}&api-key={api}'.format(section_name = section, page = page, source = source, start = start, end = end, api = key)
#     resp = requests.get(url=url)
#     data = json.loads(resp.text)
#     df = pd.DataFrame(data['response']['docs'])
#     df = NYT_dataframe_clean(df)
#     df['param'] = section
#     df['image_url'] = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHEtiVXw8Wi1tp56Nzd5rH_EoOAJA2RInEWvf5h5CQ-6O_YZp7dw'
#     return df

def NYT_api_call_parameter_ALLTIME(param, page, key):
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q={param}&page={page}&sort=newest&&api-key={api}'.format(param = param, page = page, api = key)
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    df = pd.DataFrame(data['response']['docs'])
    df = NYT_dataframe_clean(df)
    df['param_1'] = param
    df['image_url'] = 'https://greaterbostonhcs.com/wp-content/uploads/2016/05/Nutrition.jpg'
    return df

def intermediate_get_categories(df, categories):
    topics = []
    topics2 = []
    topics3 = []
    topics4 = []
    for index, row in df.iterrows():
        try:
            categories_dict = find_categories(row.description, categories)
            topics.append(categories_dict[1])
            topics2.append(categories_dict[2])
            topics3.append(categories_dict[3])
            topics4.append(categories_dict[4])
        except:
            topics.append('null')
            topics2.append('null')
            topics3.append('null')
            topics4.append('null')
    df['param_2'] = topics
    df['param_3'] = topics2
    df['param_4'] = topics3
    df['param_5'] = topics4
    return df

def NYT_pull(categories):
    empty = pd.DataFrame()
    for word in categories:
        try:
            df = NYT_api_call_parameter_ALLTIME(word,0,nyt_api_key)
            empty = empty.append(df, sort=True)
            print('Pulled '+word)
            time.sleep(2)
        except:
            print(word + " EXCEPTION!!!!")
    empty = empty.drop(['abstract','section_name'],axis = 1)
    empty = empty.rename(index=str, columns={"_id": "source_id", "document_type": "medium",'pub_date':'date','snippet':'description','word_count':'length'})
    empty['source_id'] = 'The New York Times API'
    dataframe = intermediate_get_categories(empty, categories)
    return dataframe

#NEWSAPI

def rename_columns(df):
    df = df.rename(index=str, columns={'publishedAt':'date','url':'web_url','urlToImage':'image_url'})
    return df

def add_words(df):
    lengths = []
    for string in df.content:
        try:
            lengths.append(round(int(string[string.find('+')+1:string.find(' chars')]) / 4 / 250))
        except:
            lengths.append(4)
    return lengths

def split_source_info(list_of_dicts):
    for item in list_of_dicts:
        item['source_id'] = item['source']['id']
        item['source'] = item['source']['name']

def pull_articles(parameter):
    article_results_rel = newsapi.get_everything(q=parameter,sort_by = 'relevancy',language='en', page_size=10, sources=sources_joined)
    article_results_rel = article_results_rel['articles']
    split_source_info(article_results_rel)
    return article_results_rel

def clean_articles(list_of_dicts, search_param):
    df = pd.DataFrame(list_of_dicts)
    try:
        df['medium'] = 'text'
        df['source_id'] = 'NewsAPI'
        df['param_1'] = search_param
        df['publishedAt'] = df['publishedAt'].apply(lambda x: pd.to_datetime(x).date().strftime('%Y-%m-%d'))
        df['formality'] = 'Intermediate'
        df['difficulty'] = random_difficulties(len(df['formality']))
        df['length'] = add_words(df)
        df = rename_columns(df)
        print(search_param)
    except:
        pass
    return df


def call_news_api(categories):
    empty_df = pd.DataFrame()
    for category in categories:
        dicts = pull_articles(category)
        df = clean_articles(dicts, category)
        try:
            empty_df = empty_df.append(df, sort=True)
        except:
            pass
        print(len(empty_df.index))
    df = intermediate_get_categories(empty_df, categories)
    return df
