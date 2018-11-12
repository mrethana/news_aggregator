from etl import *
from models import *
from __init__ import session
import time
from __init__ import *
from intermediate import *

new_medium_objects = []
new_provider_objects = []
new_content_objects = []
new_category_objects = []
new_expertise_objects = []

all_medium_titles = {medium.name:medium for medium in session.query(Medium).all()}
all_provider_titles = {provider.name: provider for provider in session.query(Provider).all()}
all_content_titles = {content.content_url: content for content in session.query(Content).all()}
all_category_titles = {category.name: category for category in session.query(Category).all()}
all_expertise_titles = {expertise.type: expertise for expertise in session.query(Expertise).all()}


def find_or_create_medium(medium_name):
    if medium_name in all_medium_titles.keys():
        return all_medium_titles[medium_name]
    else:
        name = medium_name
        object = Medium(name = name)
        new_medium_objects.append(object)
        all_medium_titles[medium_name] = object
        return object

def find_or_create_expertise(expertise_name):
    if expertise_name in all_expertise_titles.keys():
        return all_expertise_titles[expertise_name]
    else:
        name = expertise_name
        object = Expertise(type = name)
        new_expertise_objects.append(object)
        all_expertise_titles[expertise_name] = object
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

def find_or_create_provider(provider_name, api_id, expertise_name):
    if provider_name in all_provider_titles.keys():
        return all_provider_titles[provider_name]
    else:
        name = provider_name
        expertise = find_or_create_expertise(expertise_name)
        object = Provider(name = name, api_id=api_id, expertise = expertise)
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
            provider = find_or_create_provider(row.source, row.source_id, row.expertise) #Provider(provider_name = 'The New York Times', newsapi_id='the-new-york-times')
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
def add_expertise_objects():
    for expertise in new_expertise_objects:
        session.add(expertise)
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

print('Diet search...')
diet = intermediate_search()
find_or_create_content(diet)

add_medium_objects()
add_provider_objects()
add_content_objects()
