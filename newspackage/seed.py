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
from blogs import *
from moocs import *
warnings.filterwarnings("ignore")

new_medium_objects = []
new_provider_objects = []
new_content_objects = []
new_category_objects = []
new_formality_objects = []
new_difficulty_objects = []
new_content_category_objects = []

all_medium_titles = {medium.name:medium for medium in session.query(Medium).all()}
all_provider_titles = {provider.name: provider for provider in session.query(Provider).all()}
all_content_titles = {content.content_url: content for content in session.query(Content).all()}
all_category_titles = {category.name: category for category in session.query(Category).all()}
all_formality_titles = {formality.type: formality for formality in session.query(Formality).all()}
all_difficulty_titles = {difficulty.type: difficulty for difficulty in session.query(Difficulty).all()}


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

def find_or_create_difficulty(difficulty_name):
    if difficulty_name in all_difficulty_titles.keys():
        return all_difficulty_titles[difficulty_name]
    else:
        name = difficulty_name
        object = Difficulty(type = name)
        new_difficulty_objects.append(object)
        all_difficulty_titles[difficulty_name] = object
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


def find_or_create_content(content_url, df):
    if content_url in all_content_titles.keys():
        return all_content_titles[content_url]
    else:
        for index, row in df.iterrows():
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
            # category = find_or_create_category(row.param)
            difficulty = find_or_create_difficulty(row.difficulty)
            content_obj = Content(content_url=content_url, image_url=image_url, title=title, published = published,medium = medium,provider=provider, length = length, difficulty=difficulty)
            print(content_obj)
            all_content_titles[title] = content_obj
            new_content_objects.append(content_obj)
            return content_obj

def find_or_create_content_categories(dataframe):
    for index, row in dataframe.iterrows():
        if row.web_url in all_content_titles.keys():
            pass
        else:
            df = dataframe[(dataframe.web_url == row.web_url)]
            category_1 = find_or_create_category(row.param_1)
            category_2 = find_or_create_category(row.param_2)
            category_3 = find_or_create_category(row.param_3)
            category_4 = find_or_create_category(row.param_4)
            category_5 = find_or_create_category(row.param_5)
            content_obj = find_or_create_content(row.web_url, df)
            obj_1 = ContentCategory(value = 1,content=content_obj,category=category_1)
            new_content_category_objects.append(obj_1)
            obj_2 = ContentCategory(value = 2,content=content_obj,category=category_2)
            new_content_category_objects.append(obj_2)
            obj_3 = ContentCategory(value = 3,content=content_obj,category=category_3)
            new_content_category_objects.append(obj_3)
            obj_4 = ContentCategory(value = 4,content=content_obj,category=category_4)
            new_content_category_objects.append(obj_4)
            obj_5 = ContentCategory(value = 5,content=content_obj,category=category_5)
            new_content_category_objects.append(obj_5)
            print(obj_1)


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
def add_difficulty_objects():
    for difficulty in new_difficulty_objects:
        session.add(difficulty)
        session.commit()

def add_content_objects():
    for content in new_content_objects:
        session.add(content)
        print(content)
        session.commit()

def add_content_category_objects():
    for object in new_content_category_objects:
        session.add(object)
        session.commit()


# print('Intermediate text search...')
# print('Everyday Health')
# EH = scrape_everyday_health(nutrition_cats)
# find_or_create_content_categories(EH)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()


# print('News API')
# NAPI = call_news_api(nutrition_cats)
# find_or_create_content_categories(NAPI)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()
#
# print("NYT API")
# NYTAPI = NYT_pull(nutrition_cats)
# find_or_create_content_categories(NYTAPI)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()
#
# print('Tweets search...')
# tweets = twitter_api_call(twitter_handles, nutrition_cats)
# find_or_create_content_categories(tweets)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()
# add_content_category_objects()
#
#
# print('Youtube Search...')
# videos = youtube_api_call(youtube_searches, nutrition_cats)
# find_or_create_content_categories(videos)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()
#
# print('Podcast Search...')
# podcasts = call_podcast_api(nutrition_cats, podcast_names)
# find_or_create_content_categories(podcasts)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()

# print('Ebook Search....')
# ebooks = call_ebook_api(nutrition_cats)
# find_or_create_content_categories(ebooks)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()
#
# print('Movie Search....')
# movies = call_movie_api(movie_list,nutrition_cats)
# find_or_create_content_categories(movies)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()
#
# print('Audiobook Search....')
# audiobooks = call_audiobook_api(nutrition_cats)
# find_or_create_content_categories(audiobooks)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()
#
# print('Facebook Search....')
# fb_vid = create_sample_fb(nyt_fb_vid, nutrition_cats, 'video')
# find_or_create_content_categories(fb_vid)
# fb_posts = create_sample_fb(nyt_fb_post, nutrition_cats, 'text')
# find_or_create_content_categories(fb_posts)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()
#
# print('Instagram Search....')
# insta = create_sample_insta(insta_post, nutrition_cats)
# find_or_create_content_categories(insta)
# add_medium_objects()
# add_provider_objects()
# add_content_objects()
# add_category_objects()
# add_formality_objects()
# add_difficulty_objects()

print('UDEMY search....')
udemy = create_sample_udemy(udemy_dummy, nutrition_cats)
find_or_create_content_categories(udemy)
add_medium_objects()
add_provider_objects()
add_content_objects()
add_category_objects()
add_formality_objects()
add_difficulty_objects()
