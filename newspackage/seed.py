from etl import *
from models import *
from __init__ import session
import time
from __init__ import *
from intermediate import *
from social import *
from youtube_data import *
import warnings
from info import *
from itunes import *
warnings.filterwarnings("ignore")

new_medium_objects = []
new_provider_objects = []
new_content_objects = []
new_category_objects = []
new_formality_objects = []

all_medium_titles = {medium.name:medium for medium in session.query(Medium).all()}
all_provider_titles = {provider.name: provider for provider in session.query(Provider).all()}
all_content_titles = {content.content_url: content for content in session.query(Content).all()}
all_category_titles = {category.name: category for category in session.query(Category).all()}
all_formality_titles = {formality.type: formality for formality in session.query(Formality).all()}


def find_or_create_medium(medium_name):
    if medium_name in all_medium_titles.keys():
        return all_medium_titles[medium_name]
    else:
        name = medium_name
        object = Medium(name = name)
        new_medium_objects.append(object)
        all_medium_titles[medium_name] = object
        return object

def find_or_create_formality(formality_name):
    if formality_name in all_formality_titles.keys():
        return all_formality_titles[formality_name]
    else:
        name = formality_name
        object = Formality(type = name)
        new_formality_objects.append(object)
        all_formality_titles[formality_name] = object
        return object

def find_or_create_category(category_name):
    if category_name in all_category_titles.keys():
        return all_category_titles[category_name]
    else:
        name = category_name
        object = Category(name = name)
        new_category_objects.append(object)
        all_category_titles[category_name] = object
        return object

def find_or_create_provider(provider_name, api_id, formality_name):
    if provider_name in all_provider_titles.keys():
        return all_provider_titles[provider_name]
    else:
        name = provider_name
        formality = find_or_create_formality(formality_name)
        object = Provider(name = name, api_id=api_id, formality = formality)
        new_provider_objects.append(object)
        all_provider_titles[provider_name] = object
        return object


def find_or_create_content(dataframe):
    for index, row in dataframe.iterrows():
        if row.web_url in all_content_titles.keys():
            pass
        else:
            # print(row.title)
            content_url = row.web_url
            image_url = row.image_url
            description = str(row.description)
            title = row.title
            published = row.date
            # param = row.search_term
            length = row.length
            medium = find_or_create_medium(row.medium)#Medium(name = 'text')
            provider = find_or_create_provider(row.source, row.source_id, row.formality) #Provider(provider_name = 'The New York Times', newsapi_id='the-new-york-times')
            category = find_or_create_category(row.param)
            content_obj = Content(content_url=content_url, image_url=image_url, title=title, published = published,medium = medium,provider=provider, length = length, category = category)
            print(content_obj)
            all_content_titles[title] = content_obj
            new_content_objects.append(content_obj)



def add_medium_objects():
    for medium in new_medium_objects:
        session.add(medium)
        session.commit()

def add_provider_objects():
    for provider in new_provider_objects:
        session.add(provider)
        session.commit()
def add_formality_objects():
    for formality in new_formality_objects:
        session.add(formality)
        session.commit()

def add_category_objects():
    for category in new_category_objects:
        session.add(category)
        session.commit()

def add_content_objects():
    for content in new_content_objects:
        session.add(content)
        print(content)
        session.commit()

# print('Intermediate text search...')
# print('News API')
# NAPI = call_news_api(nutrition_cats)
# find_or_create_content(NAPI)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
#
# print("NYT API")
# NYTAPI = NYT_pull(nutrition_cats)
# find_or_create_content(NYTAPI)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
#
# print('Tweets search...')
# tweets = twitter_api_call(twitter_handles, nutrition_cats)
# find_or_create_content(tweets)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
#
# print('Youtube Search...')
# videos = youtube_api_call(youtube_searches, nutrition_cats)
# find_or_create_content(videos)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()

print('Podcast Search...')
podcasts = call_podcast_api(nutrition_cats, podcast_names)
find_or_create_content(podcasts)
add_medium_objects()
add_provider_objects()
add_content_objects()
add_category_objects()
add_formality_objects()
