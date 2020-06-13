import requests
import json
import urllib.request
import praw
import random

reddit = praw.Reddit(client_id='lIwhm8aNKKH4BQ',
                     client_secret='VrI0rAVzIeOuZVV_SYiR0jXZiA4',
                     user_agent='bot-o-meme by TheWizzy1547')


def get_memes_urls(limit=10):

    req_subreddits = ["memes", "dankmemes"]  # subreddits
    meme_list = []
    for req_subreddit in req_subreddits:
        subreddit = reddit.subreddit(req_subreddit)
        for submission in subreddit.top(limit=(limit//len(req_subreddits)) + 100):
            meme_list.append(
                ["https://reddit.com" + submission.permalink, submission.title, submission.url])
        

    random.shuffle(meme_list)  # to shuffle obtained posts
    return meme_list[:1]

# print(get_memes_urls(limit=1))
