import oauth2
import urllib
import urllib2
import json
from load_data import get_config

def oauth_req(url, http_method="POST", post_body=None, http_headers=None):
    config = get_config()
    consumer = oauth2.Consumer(key=config.get('consumer_key'), secret=config.get('consumer_secret'))
    token = oauth2.Token(key=config.get('access_token'), secret=config.get('access_token_secret'))
    client = oauth2.Client(consumer, token)

    resp, content = client.request(
        url,
        method=http_method,
        body=post_body or '',
        headers=http_headers
      )
    return content

def post_data(text):
    url = 'https://api.twitter.com/1.1/statuses/update.json?'

    data = {'status': text}
    url += urllib.urlencode(data)
    response = oauth_req(url)
    jsonData = json.loads(response)
    if 'errors' in jsonData:
        print "API Error"
        print jsonData['errors']
#end
