import requests
import json
import urllib.request
import praw
import random
import os

PRAW_CLIENT_ID = os.environ['PRAW_CLIENT_ID']
PRAW_CLIENT_SECRET = os.environ['PRAW_CLIENT_SECRET']
PRAW_USERAGENT = os.environ['PRAW_USERAGENT']


reddit = praw.Reddit(client_id=PRAW_CLIENT_ID,
                     client_secret=PRAW_CLIENT_SECRET,
                     user_agent=PRAW_USERAGENT)


def get_memes_urls(limit=10):

    req_subreddits = ["memes", "dankmemes"]  # subreddits
    meme_list = []
    for req_subreddit in req_subreddits:
        subreddit = reddit.subreddit(req_subreddit)
        for submission in subreddit.hot(limit=(limit//len(req_subreddits)) + 50):
            meme_list.append(
                ["https://reddit.com" + submission.permalink, submission.title, submission.url])
        

    random.shuffle(meme_list)  # to shuffle obtained posts
    return meme_list[:1]

# print(get_memes_urls(limit=1))
