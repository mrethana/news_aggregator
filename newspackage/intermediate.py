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

today = int(str(date.today()).replace('-',''))
last_week = int(str(date.today() - datetime.timedelta(days = 14)).replace('-',''))

def NYT_title_clean(df):
    titles = []
    for index, row in df.iterrows():
        title = row.headline['main']
        titles.append(title)
    df['title'] = titles
    return df

def NYT_dropped_rows(df):
    df = df.drop(['blog','byline','headline','keywords','multimedia','news_desk','print_page','score','type_of_material','uri'],axis =1)
    df.pub_date = pd.to_datetime(df.pub_date).dt.date
    df.word_count = round(df.word_count / 150)
    df.document_type = 'text'
    df['expertise'] = 'Intermediate'
    return df

def NYT_dataframe_clean(df):
    dataframe = NYT_title_clean(df)
    dataframe = NYT_dropped_rows(dataframe)
    return dataframe

def NYT_api_call_section_based(section, source, page, start, end, key):
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=section_name:({section_name})&page={page}&source:({source})&begin_date={start}&end_date={end}&api-key={api}'.format(section_name = section, page = page, source = source, start = start, end = end, api = key)
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    df = pd.DataFrame(data['response']['docs'])
    df = NYT_dataframe_clean(df)
    df['param'] = section
    df['image_url'] = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHEtiVXw8Wi1tp56Nzd5rH_EoOAJA2RInEWvf5h5CQ-6O_YZp7dw'
    return df

def NYT_api_call_parameter_ALLTIME(param, page, key):
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q={param}&page={page}&sort=newest&&api-key={api}'.format(param = param, page = page, api = key)
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    df = pd.DataFrame(data['response']['docs'])
    df = NYT_dataframe_clean(df)
    df['param'] = param
    df['image_url'] = 'https://theindianspot.com/wp-content/uploads/2017/09/KETO-DIET-ALL-YOU-WANT-TO-KNOW.jpg'
    return df

def diet_NYT():
    empty = pd.DataFrame()
    for word in ['keto','ketogenic','paleo','vegan','vegetarian']:
        df = NYT_api_call_parameter_ALLTIME(word,0,nyt_api_key)
        empty = empty.append(df, sort=True)
        print('Pulled '+word)
        time.sleep(2)
    empty = empty.drop(['abstract','section_name'],axis = 1)
    empty = empty.rename(index=str, columns={"_id": "source_id", "document_type": "medium",'pub_date':'date','snippet':'description','word_count':'length'})
    return empty

# def general_health():
#     empty = pd.DataFrame()
#     for page in [0,1]:
#         df = NYT_api_call_section_based('Health', 'The New York Times',page, last_week, today, nyt_api_key)
#         empty = empty.append(df)
#         time.sleep(2)
#     return empty

def intermediate_search():
    # df1 = general_health()
    df2 = diet_NYT()
    # frames = [df1,df2]
    # result = pd.concat(frames)
    return df2 #result
