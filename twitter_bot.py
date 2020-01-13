import tweepy
import time

# global variables
LAST_TEXT_FILE_NAME = 'last_seen_id.txt'
C_KEY_FILE = 'consumer_key.txt'
C_SECRET_FILE = 'consumer_secret.txt'
A_KEY_FILE = 'access_key.txt'
A_SECRET_FILE = 'access_secret.txt'

TWEET_HEADER = 'Our spotlight today is '
MAX_TWEET_LEN = 280
MENTION_LEN = len('@dailyshoutout4')


# FUNCTIONS
def get_keys (file_name):
    f_read = open(file_name, 'r')
    return f_read.read()
    
# prevent the same mention from being read again
def retrieve_last_seen_id (file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# store the last seen id
def store_last_seen_id (last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# replies to the tweets
def reply_to_tweets():
    print('retrieving and replying to tweets...')

    # get the last seen id
    last_seen_id = retrieve_last_seen_id(LAST_TEXT_FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id,
                                tweet_mode='extended')

    # prevent shoutout if there is nothing to shoutout
    if len(mentions) == 0:
        return

    # get the tweet to shout out
    shoutout = mentions[len(mentions) - 1]
    status = process_string(shoutout)

    # cut description up if tweet is too long
    iterations = len(status) / MAX_TWEET_LEN
    iterations += 1

    # post shoutouts
    for i in range(int(iterations)):
        api.update_status(status[(i * MAX_TWEET_LEN):
                        ((i + 1) * MAX_TWEET_LEN)], shoutout.id)

# processes string so @dailyshoutout4 is not included
def process_string (shoutout):
    
    print(str(shoutout.id) + ' - ' + shoutout.full_text) 
    last_seen_id = shoutout.id
    store_last_seen_id(last_seen_id, LAST_TEXT_FILE_NAME)
    
    # extract the text desciption from the shoutout
    description = shoutout.full_text
    start_index = description.lower().index('@dailyshoutout4')
    description = (description[0:start_index] +
                   description[start_index + MENTION_LEN:
                               len(description) - 1])
 

    # create the full length of the tweet
    status = (TWEET_HEADER + '@' + shoutout.user.screen_name + '\n' 
                        + description)

    return status

# get API keys
CONSUMER_KEY = get_keys(C_KEY_FILE)
CONSUMER_SECRET = get_keys(C_SECRET_FILE)
ACCESS_KEY = get_keys(A_KEY_FILE)
ACCESS_SECRET = get_keys(A_SECRET_FILE)

# create the api object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# get the timeline info from the most recent mentions
mentions = api.mentions_timeline()

# prints the attributes of the most recent mention
print(mentions[0].__dict__.keys())

# prints the text of the most recent mention
print(mentions[0].text)    

while True:
    reply_to_tweets()
    time.sleep(43200)