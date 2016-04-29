import datetime
import json
import random

import praw


def RedditData(query):
    time = "year"
    query = query.replace(" ","+")
    print query
    r = praw.Reddit(user_agent='my_cool_application')
    submissions = r.search(query, subreddit="uiuc", sort=None, syntax=None, period=time)
    subreddit_posts = list()
    for x in submissions:
       time = x.created
       datetimes = datetime.datetime.fromtimestamp(time)
       subreddit_posts.append({"subreddit": "r/UIUC", "url": x.url, "title": x.title, "datetime": str(datetimes), "comments": random.randint(1, 10), "points": random.randint(1, 50)})

    data_str = json.dumps(subreddit_posts)
    print data_str
    return data_str