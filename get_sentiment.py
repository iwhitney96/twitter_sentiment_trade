import json
import argparse
import re
from watson_developer_cloud import AlchemyLanguageV1

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
    alchemy_language = AlchemyLanguageV1(api_key='ae2125f5f990fa0a81af8ad297b0cda45ffffe29')
    tweet = ''
    for x in range(0, len(inputDict)):
        for y in inputDict[x]:
            tweet+=y
    #end loop
    processedTweets = processText(tweet)
    processedTweets = 'text=' + processedTweets
    return json.dumps(
        alchemy_language.combined(
        processedTweets,
        extract='doc-sentiment,entities',
        sentiment=1,
        max_items=8),
        indent=2)
#end
