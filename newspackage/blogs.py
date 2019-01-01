import requests
import re
import numpy as np
import time
from bs4 import BeautifulSoup
import pandas as pd
from info import *
from nltk.tokenize import RegexpTokenizer


#EVERYDAY HEALTH
def search_everyday_health(term):
    html_page = requests.get('https://www.everydayhealth.com/search/%s/?iid=gnav_head_search'%term)
    soup = BeautifulSoup(html_page.content, 'html.parser', from_encoding='utf-8')
    results = soup.findAll('a')
    dates = [pd.to_datetime(date.text).date().strftime('%Y-%m-%d') for date in soup.findAll("div", class_="resultDate")]
    results = [result.get('href') for result in results]
    results = ['https:'+result for result in results if str(result)[:6] == '//www.' if 'search' not in result if term in result]
    return results, dates

def tokenize_text(text):
    tokenizer = RegexpTokenizer('[A-Za-z]\w+')
    all_tokens = tokenizer.tokenize(text)
    text = " ".join(all_tokens)
    return text

def scrape_articles(results,dates,term, categories):
    df = pd.DataFrame(results,columns=['web_url'])
    all_text = []
    all_titles = []
    all_lengths = []
    all_categories2 = []
    all_categories3 = []
    all_categories4 = []
    all_categories5 = []
    for result in results:
        html_page = requests.get(result)
        soup = BeautifulSoup(html_page.content, 'html.parser', from_encoding="iso-8859-1")
        all_titles.append(soup.title.string)
#         author = soup.find("h3", class_="byline_text").text.replace('By','').strip()
        article = soup.findAll('p')
        body = tokenize_text(article[3].text)
        all_text.append(body)
        category_dict = find_categories(body, categories)
        all_categories2.append(category_dict[1])
        all_categories3.append(category_dict[2])
        all_categories4.append(category_dict[3])
        all_categories5.append(category_dict[4])
        length = len(body) /4/ 250
        if length > 5:
            all_lengths.append(length)
        else:
            all_lengths.append(5)
    df['description'] = all_text
    df['title'] = all_titles
    df['image_url'] = 'https://static1.squarespace.com/static/5ab11d8f75f9ee24a7bf7183/t/5b855f85758d46c5adb43368/1535563805366/EDH.png'
    df['length'] = all_lengths
    df['source'] = 'Everyday Health'
    df['source_id'] = 'Blog'
    df['formality'] = 'Intermediate'
    df['medium'] = 'text'
    df['date'] = dates
    df['param_1'] = term
    df['param_2'] = all_categories2
    df['param_3'] = all_categories2
    df['param_4'] = all_categories2
    df['param_5'] = all_categories2
    df['difficulty'] = random_difficulties(len(df['title']))
    return df

def scrape_everyday_health(categories):
    empty = pd.DataFrame()
    for category in categories:
        print(category)
        try:
            results, dates = search_everyday_health(category)
            df = scrape_articles(results, dates, category, categories)
            empty = empty.append(df, sort=True)
            print('SUCCESS!')
        except:
            print('EXCEPTION')
    return empty
