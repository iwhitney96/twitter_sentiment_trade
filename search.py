import get_twitter_data
from get_sentiment import sentiment_retrieve

keyword = 'trump'
time = 'today'
twitterData = get_twitter_data.TwitterData()
tweets = twitterData.getTwitterData(keyword, time)
print tweets
sentiment = sentiment_retrieve(tweets)
print sentiment
