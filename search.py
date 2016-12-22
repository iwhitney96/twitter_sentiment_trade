import get_twitter_data

keyword = 'iphone'
time = 'today'
twitterData = get_twitter_data.TwitterData()
tweets = twitterData.getTwitterData(keyword, time)
for x in tweets:
    for y in tweets[x]:
        print y
#end loop

#print tweets
