from info import *
import random
import pandas as pd
import requests
import datetime
from datetime import date


udemy_dummy = [('https://www.udemy.com/cognitive-behavioural-therapy-online-course-cbt-practitioner-course/','Udemy','video'),
('https://www.udemy.com/closecombattraining/','Udemy','video'),
              ('https://www.udemy.com/become-a-superhuman-naturally-safely-boost-testosterone/','Udemy','video'),
              ('https://www.udemy.com/internationally-accredited-diploma-certificate-in-nutrition/','Udemy','video'),
              ('https://www.udemy.com/nutrition-masterclass-build-your-perfect-diet-meal-plan/','Udemy','video'),
              ('https://www.udemy.com/whole-food-plant-based-diet/','Udemy','video'),
         ('https://www.udemy.com/health-and-nutrition-life-coach-certification/','Udemy','video')]

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



def create_sample_udemy(list_tuples, categories_list):
    diets = ['vegan','keto','vegetarian','paleo']
    df = pd.DataFrame()
    df['description'] = 'Udemy Dummy Data'
    df['title'] = 'Udemy Dummy Data'
    df['date'] = '2018-12-26'
    # df['medium'] = medium_type
    # df['source'] = 'NYT Health'
    df['source_id'] = 'Udemy'
    df['formality'] = 'Formal'
    length = len(df.title)
    df['difficulty'] = random_difficulties(length)
    df['length'] = random_length(length)
    df['param_1'] = random_cat(diets,length)
    df['param_2'] = random_cat(categories_list,length)
    df['param_3'] = random_cat(categories_list,length)
    df['param_4'] = random_cat(categories_list,length)
    df['param_5'] = random_cat(categories_list,length)
    urls = []
    images = []
    sources = []
    mediums = []
    for tuple in list_tuples:
        urls.append(tuple[0])
        images.append(tuple[0])
        sources.append(tuple[1])
        mediums.append(tuple[2])
    df['source'] = sources
    df['web_url'] = urls
    df['image_url'] = images
    df['medium'] = mediums
    return df
