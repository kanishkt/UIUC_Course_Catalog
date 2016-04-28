import datetime
import json
import praw


def RedditData(query, time):
    r = praw.Reddit(user_agent='my_cool_application')
    submissions = r.search(query, subreddit="uiuc", sort=None, syntax=None, period=time)
    subreddit_posts = list()
    for x in submissions:
       points = x.ups - x.downs
       time = x.created
       datetimes = datetime.datetime.fromtimestamp(time)
       subreddit_posts.append({"subreddit": "r/UIUC", "url": x.url, "title": x.title, "datetime": str(datetimes), "comments": 10, "points": points})

    data_str = json.dumps(subreddit_posts)
    print data_str

if __name__ == '__main__':
    RedditData()