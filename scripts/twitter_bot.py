import tweepy
import time

# global variables
#LAST_TEXT_FILE_NAME = 'last_seen_id.txt'
#C_KEY_FILE = 'consumer_key.txt'
#C_SECRET_FILE = 'consumer_secret.txt'
#A_KEY_FILE = 'access_key.txt'
#A_SECRET_FILE = 'access_secret.txt'

#TWEET_HEADER = 'Our spotlight today is '
#MAX_TWEET_LEN = 280
#MENTION_LEN = len('@dailyshoutout4')

class ShoutoutBot:

    def __init__(self, api, stream):
        self.api = api
        self.stream = stream
        print("constructed")

    # replies to the tweets
    def reply_to_tweets(self, file_name, max_len, header):
        """takes file containing tweet and tweets contents"""

        print('retrieving and replying to tweets...')

        # get the last seen id
        last_seen_id = self.stream.retrieve_last_seen_id(file_name)
        mentions = self.api.mentions_timeline(last_seen_id,
                                    tweet_mode='extended')

        # prevent shoutout if there is nothing to shoutout
        if len(mentions) == 0:
            return

        # get the tweet to shout out
        shoutout = mentions[len(mentions) - 1]
        status = self.process_string(shoutout, file_name, header)

        # cut description up if tweet is too long
        iterations = len(status) / max_len
        iterations += 1

        # post shoutouts
        for i in range(int(iterations)):
            self.api.update_status(status[(i * max_len):
                            ((i + 1) * max_len)], shoutout.id)

    # processes string so @dailyshoutout4 is not included
    def process_string (self, shoutout, file_name, header):
        """processes the content of the shoutout"""
        
        print(str(shoutout.id) + ' - ' + shoutout.full_text) 
        last_seen_id = shoutout.id
        self.stream.store_last_seen_id(last_seen_id, file_name)
        
        # extract the text desciption from the shoutout
        description = shoutout.full_text
        start_index = description.lower().index('@dailyshoutout4')
        description = (description[0:start_index] +
                    description[start_index + len('@dailyshoutout4'):
                                len(description) - 1])
    

        # create the full length of the tweet
        status = (header + '@' + shoutout.user.screen_name + '\n' 
                            + description)

        return status


