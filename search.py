import get_twitter_data
import json
import csv
from get_sentiment import sentiment_retrieve
from send_email import send_email
#from post_twitter_data import post_data

keyword = '$AAPL'
stock = 'Apple'



twitterData = get_twitter_data.TwitterData()
tweets = twitterData.getTwitterData(keyword, 'pastthree', 'search')
sentiment1 = sentiment_retrieve(tweets)
print sentiment1['docSentiment']['score']
tweets = twitterData.getTwitterData(keyword, 'beginweek', 'search')
sentiment2 = sentiment_retrieve(tweets)
print sentiment2['docSentiment']['score']

docsentiment1 = float(sentiment1['docSentiment']['score'])
docsentiment2 = float(sentiment2['docSentiment']['score'])


#twitterData.post_data('Hello World!')

subject = "Automated Weelock Capital Update for " + stock
text = "Hello,\n\n Stock: %s\nKeyword: %s\nWeeklong Sentiment: %f\nSentiment over the past three days: %f\nChange : %f\n\nBest,\nWCM System" % (stock, keyword, docsentiment1, docsentiment2, docsentiment2 - docsentiment1)
send_email("Automated Weelock Capital Update", text)



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
