import get_twitter_data
import json
import csv
from get_sentiment import sentiment_retrieve

keyword = '$AAPL'


twitterData = get_twitter_data.TwitterData()

#remember cashtag idea
tweets = twitterData.getTwitterData(keyword, 'pastthree', 'general')
sentiment = sentiment_retrieve(tweets)
print sentiment['docSentiment']['score']
tweets = twitterData.getTwitterData(keyword, 'beginweek', 'general')
sentiment = sentiment_retrieve(tweets)
print sentiment['docSentiment']['score']



#for x in sp500:
#    for y in range(0,6):
#        x.append(doc_sentiment)

'''
twitterData = get_twitter_data.TwitterData()
tweets = twitterData.getTwitterData(keyword, time, 'news-sources1')
print tweets
#example flow
#twitterData = get_twitter_data.TwitterData()
#tweets = twitterData.getTwitterData(keyword, time, 'news-sources1')
#print tweets

sentiment = sentiment_retrieve(tweets)
print sentiment
'''
