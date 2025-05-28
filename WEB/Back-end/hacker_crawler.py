import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# Ref : https://softwaree.tistory.com/74 [Owl Life:티스토리]
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "hn_crawling_experiment.settings")

import django

django.setup()
from main.models import StoryData

def fetch_hacker_latest_id():
    result = []

    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty' # API: top stories
    response = requests.get(url) # already in json(API)
    id_list = response.json() # read as json

    maximum_crawl = 10 # test reason(limits the amount of data to crawl)
    for various_id in id_list:
        specific_url = 'https://hacker-news.firebaseio.com/v0/item/' + str(various_id) + '.json?print=pretty'
        raw_id = requests.get(specific_url) # already in json(API)
        specific_id = raw_id.json() # read as json

        if maximum_crawl == 0: # limit(stop crawling)
            break

        by = specific_id['by']
        try: # check for empty variables
            descendants = specific_id['descendants']
        except KeyError:
            descendants = None
        id = specific_id['id']
        score = specific_id['score']

        time_stamp = specific_id['time'] # timestamp format
        time = datetime.fromtimestamp(time_stamp)  # from timestamp to datetime format TODO: fix warning on 'naive datetime'

        title = specific_id['title']
        type = specific_id['type']
        try: # check for empty variables
            url = specific_id['url']
        except KeyError:
            url = None

        story_obj = {
            'by': by,
            'descendants': descendants,
            'id': id,
            'score': score,
            'time': time,
            'title': title,
            'type': type,
            'url': url,
        }
        print(str(maximum_crawl) + '. ' + title)
        result.append(story_obj)

        maximum_crawl = maximum_crawl - 1 # count
    return result

def add_new_items(crawled_stories):
    last_inserted_story = StoryData.objects.last()
    if last_inserted_story is None:
        last_inserted_id = ""
    else:
        last_inserted_id = getattr(last_inserted_story, 'id')

    items_to_insert_into_db = []

    for story in crawled_stories:
        if story['id'] == last_inserted_id: # check if it is the end
            break
        items_to_insert_into_db.append(story)
    items_to_insert_into_db.reverse() # new story at the top

    for story in items_to_insert_into_db:
        print("new story added!!! : " + str(story['id']) + '. ' + story['title'])

        StoryData(by=story['by'],
                  descendants=story['descendants'],
                  post_id=story['id'],
                  score=story['score'],
                  time=story['time'],
                  title=story['title'],
                  url=story['url']).save()

    return items_to_insert_into_db

if __name__ == '__main__':
    add_new_items(fetch_hacker_latest_id())