import sys
import twitter_bot
import stream 

# global variables
LAST_TEXT_FILE_NAME = 'last_seen_id.txt'
C_KEY_FILE = 'consumer_key.txt'
C_SECRET_FILE = 'consumer_secret.txt'
A_KEY_FILE = 'access_key.txt'
A_SECRET_FILE = 'access_secret.txt'

io = stream.IO()
key = io.get_keys(C_KEY_FILE)
assert(key == 'v5WHRfUFhVMCosNZWvqGpcHhA')

last_seen_id = io.retrieve_last_seen_id(LAST_TEXT_FILE_NAME)
assert(last_seen_id == '1213741043759243267')

