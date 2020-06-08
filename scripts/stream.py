class IO:

    def __init__(self):
        print("constructed IO")

    # FUNCTIONS
    def get_keys (self, file_name):
        """obtains authentication keys from key file"""

        f_read = open(file_name, 'r')
        return f_read.read()
        
    # prevent the same mention from being read again
    def retrieve_last_seen_id (self, file_name):
        """retrieves the id of the most recent tweet that mentions
        the twitter bot"""

        f_read = open(file_name, 'r')
        last_seen_id = int(f_read.read().strip())
        f_read.close()
        return last_seen_id

    # store the last seen id
    def store_last_seen_id (self, last_seen_id, file_name):
        """stores the id of the most recent tweet that mentions
        the twitter bot"""

        f_write = open(file_name, 'w')
        f_write.write(str(last_seen_id))
        f_write.close()
        return
