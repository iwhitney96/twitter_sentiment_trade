import get_twitter_data
from get_sentiment import sentiment_retrieve
keyword = 'Vacation'
time = 'today'

twitterData = get_twitter_data.TwitterData()
tweets = twitterData.getTwitterData(keyword, time, 'news-sources1')
print tweets

#sentiment = sentiment_retrieve(tweets)
