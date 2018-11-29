import pandas as pd

def add_scraping_source(df, identifier_dict):
    scraped_source = []
    for index, row in df.iterrows():
        identifier = row.medium + row.formality
        scraped_from = identifier_dict[identifier]
        scraped_source.append(scraped_from)
    df['scraped_from'] = scraped_source
    return df
def fix_NYT(df):
    df.loc[(df.provider=='The New York Times') & (df.medium == 'text'), 'scraped_from'] = 'NYT API'
    return df

identifier_dict = {'audioFormal':'Itunes Audiobook','textFormal':'Itunes Ebook','videoFormal':'Itunes Movie',
                  'textInformal': 'Twitter', 'videoInformal': 'Youtube',
                   'audioIntermediate': 'Itunes Podcast', 'textIntermediate': 'NewsApi', 'videoIntermediate': 'Youtube'}

df = pd.DataFrame([{'content_url':content.content_url, 'image_url':content.image_url,'title':content.title
                             , 'published': content.published, 'length': content.length, 'medium':content.medium.name,
                             'provider': content.provider.name, 'api_id':content.provider.api_id, 'formality':content.provider.formality.type,
                             'category':content.category.name} for content in session.query(Content).all()])
