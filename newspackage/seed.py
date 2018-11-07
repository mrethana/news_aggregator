from etl import *
from models import *
from __init__ import session
import time
from __init__ import *

new_medium_objects = []
new_provider_objects = []
new_content_objects = []

all_medium_titles = {medium.name:medium for medium in session.query(Medium).all()}
all_provider_titles = {provider.provider_name: provider for provider in session.query(Provider).all()}
all_content_titles = {content.content_url: content for content in session.query(Content).all()}


def find_or_create_medium(medium_name):
    if medium_name in all_medium_titles.keys():
        return all_medium_titles[medium_name]
    else:
        name = medium_name
        object = Medium(name = name)
        new_medium_objects.append(object)
        all_medium_titles[medium_name] = object
        return object


def find_or_create_provider(provider_name, newsapi_id):
    if provider_name in all_provider_titles.keys():
        return all_provider_titles[provider_name]
    else:
        name = provider_name
        api_id = newsapi_id
        object = Provider(provider_name = name, newsapi_id=api_id)
        new_provider_objects.append(object)
        all_provider_titles[provider_name] = object
        return object


def find_or_create_content(dataframe):
    for index, row in dataframe.iterrows():
        if row.url in all_content_titles.keys():
            pass
        else:
            print(row.title)
            content_url = row.url
            image_url = row.urlToImage
            # description = str(row.description)
            title = row.title
            published = row.publishedAt
            param = row.search_term
            medium = find_or_create_medium(row.medium)#Medium(name = 'text')
            provider = find_or_create_provider(row.source_name, row.source_id) #Provider(provider_name = 'The New York Times', newsapi_id='the-new-york-times')
            content_obj = Content(content_url=content_url, image_url=image_url, title=title, published = published,medium = medium,provider=provider,search_param = param)
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

def add_content_objects():
    for content in new_content_objects:
        session.add(content)
        print(content)
        session.commit()

print('Blockchain search...')
bchain = quick_search('blockchain')
find_or_create_content(bchain)

add_medium_objects()
add_provider_objects()
add_content_objects()
