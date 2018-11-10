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

def NYT_api_call(section, source, page, start, end, key):
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=section_name:({section_name})&page={page}&source:({source})&begin_date={start}&end_date={end}&api-key={api}'.format(section_name = section, page = page, source = source, start = start, end = end, api = key)
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    df = pd.DataFrame(data['response']['docs'])
    df = NYT_dataframe_clean(df)
    return df
# df2 = NYT_api_call('Health', 'The New York Times',0, last_week, today, nyt_api_key)
# df =  NYT_api_call('Health', 'The New York Times',1, last_week, today, nyt_api_key)
# df = df.append(df2)
