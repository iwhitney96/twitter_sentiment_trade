import json
import argparse
import re
import os
from load_data import get_config

from watson_developer_cloud import AlchemyLanguageV1

#thanks to Ravikiran Janardhana for the process text and get_config
#start process_tweet
def processText(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+',' ',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end


#start sentiment_retrieve
#takes inputText, processes it, and returns JSON from Watson
def sentiment_retrieve(inputDict):
    config = get_config()
    alchemy_language = AlchemyLanguageV1(api_key=config.get("alchemy_api"))
    tweet = ''
    for x in range(0, len(inputDict)):
        for y in inputDict[x]:
            tweet+=y
    #end loop
    processedTweets = processText(tweet)
    processedTweets = 'text=' + processedTweets
    return alchemy_language.combined(
        processedTweets,
        extract='doc-sentiment',
        sentiment=1,
        max_items=8)
#end
