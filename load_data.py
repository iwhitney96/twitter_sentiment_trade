import csv
import json
import os

def getSP500():
    sp500 = []
    with open('sp500.csv') as f:
        x = csv.reader(f, delimiter=',')
        for row in x:
            sp500.append(row)
    return sp500
#end


def get_config():
  config = {}
  # from file args
  if os.path.exists('config.json'):
      with open('config.json') as f:
          config.update(json.load(f))

  return config
