import json
import os
import random
import time
import tweepy
from types import SimpleNamespace

# Recover keys from enviromment
API_KEY = os.environ.get("TWEETBOT_API_KEY")
API_SECRET_KEY = os.environ.get("TWEETBOT_API_SECRET_KEY")
API_ACCESS_TOKEN = os.environ.get("TWEETBOT_ACCESS_TOKEN")
API_ACCESS_TOKEN_SECRET = os.environ.get("TWEETBOT_ACCESS_TOKEN_SECRET")

# Recover tweets
with open('tweets.json') as json_file:
    tweets = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))

# Authenticate on Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(API_ACCESS_TOKEN, API_ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

def postRandomTweet():
    try:
        # Generate random tweet id to be recovered
        randomTweet = random.randrange(0, len(tweets.tweets) - 1)

        # Create a tweet
        api.update_status(tweets.tweets[randomTweet].tweet)

        print("Tweet posted successfuly")
    except tweepy.TweepError as e:
        print(e.reason)

# Loop - timer
while True:
    postRandomTweet()
    # Sleep
    time.sleep(300)
