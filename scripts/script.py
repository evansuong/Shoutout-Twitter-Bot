import sys
import tweepy
import time
import twitter_bot
import stream


# global variables
LAST_TEXT_FILE_NAME = 'C:/Users/evans/Desktop/Projects/Python/\
Twitter Bot Tut/Shoutout-Twitter-Bot/data/last_seen_id.txt'
C_KEY_FILE = 'C:/Users/evans/Desktop/Projects/Python/Twitter Bot Tut/\
Shoutout-Twitter-Bot/data/consumer_key.txt'
C_SECRET_FILE = 'C:/Users/evans/Desktop/Projects/Python/Twitter Bot \
Tut/Shoutout-Twitter-Bot/data/consumer_secret.txt'
A_KEY_FILE = 'C:/Users/evans/Desktop/Projects/Python/Twitter Bot Tut/\
Shoutout-Twitter-Bot/data/access_key.txt'
A_SECRET_FILE = 'C:/Users/evans/Desktop/Projects/Python/Twitter Bot \
Tut/Shoutout-Twitter-Bot/data/access_secret.txt'

TWEET_HEADER = 'Our spotlight today is '
MAX_TWEET_LEN = 280
MENTION_LEN = len('@dailyshoutout4')


def run():
    """builds api authentication and tweets shoutouts every
    hour"""

    io = stream.IO()

    # get API keys
    CONSUMER_KEY = io.get_keys(C_KEY_FILE)
    CONSUMER_SECRET = io.get_keys(C_SECRET_FILE)
    ACCESS_KEY = io.get_keys(A_KEY_FILE)
    ACCESS_SECRET = io.get_keys(A_SECRET_FILE)

    print("running")

    # create the api object
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    bot = twitter_bot.ShoutoutBot(api, io)

    # get the timeline info from the most recent mentions
    mentions = api.mentions_timeline()

    # prints the attributes of the most recent mention
    print(mentions[0].__dict__.keys())

    # prints the text of the most recent mention
    print(mentions[0].text)    

    while True:
        bot.reply_to_tweets(LAST_TEXT_FILE_NAME, MAX_TWEET_LEN, 
        TWEET_HEADER)
        time.sleep(3600)

