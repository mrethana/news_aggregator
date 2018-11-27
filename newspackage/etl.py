from apikeys import *
from models import *
from __init__ import *
import pafy
import requests
import re
import numpy as np
import time
from bs4 import BeautifulSoup
import pandas as pd
from IPython.core.display import HTML, Image
import plotly.plotly as py
import plotly.graph_objs as go
from info import *



def pull_pods(parameter):
    list_dicts = []
    urls = []
    split = parameter.split()
    if len(split) < 2:
        split.append('')
    html_page = requests.get('https://tunein.com/search/?query='+split[0]+'%'+'20'+split[1])
    soup = BeautifulSoup(html_page.content, 'html.parser', from_encoding='utf-8')
    pods = soup.findAll('a')
    strings = []
    for number in list(range(0,10)):
        strings.append(str(number))
    for pod in pods[6:]:
        if pod.get('href') is not None:
            if pod.get('href')[-1] in strings:
                url = "https://tunein.com/embed/player/t"+pod.get('href')[-9:]+"/"
                data = {'author':'audio', 'content':'audio','description':'audio','publishedAt':'audio', 'source_id':'audio', 'source_name':'audio','title':'audio','url':url,'urlToImage':'audio', 'medium':'audio'}
                if url in urls:
                    pass
                else:
                    list_dicts.append(data)
                urls.append(url)
    return list_dicts


#call Twitter embed API to embed tweet in  dashboard
class Tweet(object):
    def __init__(self, s, embed_str=False):
        if not embed_str:
            # Use Twitter's oEmbed API
            # https://dev.twitter.com/web/embedded-tweets
            api = 'https://publish.twitter.com/oembed?url={}'.format(s)
            response = requests.get(api)
            self.text = response.json()["html"]
        else:
            self.text = s

    def _repr_html_(self):
        return self.text

def query_content(Limit, Medium, Formality, Max_Length, search_param):
    all_objects = [content for content in session.query(Content).order_by(desc(Content.published)).all() if content.medium.name == Medium if search_param in content.category.name if content.provider.formality.type == Formality if content.length < Max_Length]
    if len(all_objects) < 1:
        print('No Content')
    else:
        if Medium == 'text':
            if Formality != 'Informal':
                for i in range (0, Limit):
                    title = all_objects[i].title
                    link = all_objects[i].content_url
                    image = all_objects[i].image_url
                    source_name = all_objects[i].provider.name
                    display(HTML("<a href="+link+">"+source_name+': '+title+"</a>"))
                    display(Image(url = image))
            else:
                for i in range (0, Limit):
                    display(Tweet(all_objects[i].content_url))
        elif Medium == 'video':
            for i in range (0, Limit):
                title = all_objects[i].title
                link = all_objects[i].content_url
                link = link[-11:]
                source_name = all_objects[i].provider.name
                display(HTML("<a href="+link+">"+source_name+': '+title+"</a>"))
                display(HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/'+link+'?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>'))
        elif Medium == 'audio':
            for i in range (0, Limit):
                link = all_objects[i].content_url
                display(HTML("<iframe src="+"'"+link+"'"+ "style='width:100%; height:100px;' scrolling='no' frameborder='no'></iframe>"))


def count_formality_per_medium(medium, formality, param):
    return len([content for content in session.query(Content).all() if content.medium.name == medium if param in content.category.name if content.provider.formality.type == formality])

#plot stacked bar in dashboard
def plot_stacked(param):
    x = [medium.name for medium in session.query(Medium).all()]
    trace1 = go.Bar(
        x= x,
        y=[count_formality_per_medium(x[0],'Informal',param),count_formality_per_medium(x[1],'Informal',param)],
        # ,count_formality_per_medium(x[1],'Informal',param),count_formality_per_medium(x[2],'Informal',param)],
        name='Informal')

    trace2 = go.Bar(
       x = x,
       y=[count_formality_per_medium(x[0],'Intermediate',param),count_formality_per_medium(x[1],'Intermediate',param)],
#         y=[count_formality_per_medium(x[0],'Intermediate',param),count_formality_per_medium(x[1],'Intermediate',param),count_formality_per_medium(x[2],'Intermediate',param)],
        name='Intermediate')

    trace3 = go.Bar(
        x = x,
        y=[count_formality_per_medium(x[0],'Formal',param),count_formality_per_medium(x[1],'Formal',param)],
#         y=[count_formality_per_medium(x[0],'Formal',param),count_formality_per_medium(x[1],'Formal',param),count_formality_per_medium(x[2],'Formal',param)],
        name='Formal')

    data = [trace1, trace2, trace3]
    layout = go.Layout(
        barmode='stack'
    )

    fig = go.Figure(data=data, layout=layout)
    return py.iplot(fig, filename='plot from API (20)')
