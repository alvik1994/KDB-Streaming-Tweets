# KDB-Streaming-Tweets
This app will stream realtime tweets into a kdb ticker plant infrastructure

TICK
<code>q tick.q -p TICK_PORT</code>
RDB
<code>q tick/r.q :TICK_PORT :HDB_PORT -p RDB_PORT</code>
HDB
<code>q data/sym -p HDB_PORT</code>

<code>python twitter_streaming.py host port word1 word2 word3 ...</code>
