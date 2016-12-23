import argparse
import urllib
import urllib2
import json
import datetime
import random
import os
import pickle
from datetime import timedelta
import oauth2

from watson_developer_cloud import AlchemyLanguageV1


alchemy_language = AlchemyLanguageV1(api_key='ae2125f5f990fa0a81af8ad297b0cda45ffffe29')

print(json.dumps(
  alchemy_language.combined(
    text='Kellyanne Conway will be the counseler to President Trump. So happy for that!',
    extract='entities,keywords',
    sentiment=1,
    max_items=1),
  indent=2))
