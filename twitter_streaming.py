
import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from qpython import qconnection
import json
import sys

access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']


class StdOutListener(StreamListener):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        ts = data['timestamp_ms']
        text = "(),\"{}\"".format(data['text'].encode('ascii', 'ignore'))
        name = "`$ \"{}\"".format(data['user']['screen_name'].encode('ascii', 'ignore'))
        row = "(" + ";".join([ name, "utl " + ts, data['id_str'], text]) + ")"
        try:
            q.sync('.u.upd[`tweets;{}]'.format(row))
        except:
            print '.u.upd[`tweets;{}]'.format(row) + " failed"
        return True

    def on_error(self, status_code):
        print status_code

if __name__ == '__main__':
    global q
    q = qconnection.QConnection(host='localhost', port=6500)
    q.open()
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=sys.argv[1:])