# Tweet Quotes from Yaml
# Adapted from: https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, yaml, random, os

# Get environment variables (stored encrypted in github repository, and called into the OS from the action workflow file main.yml)
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

files=os.listdir('Marshall-Rosenberg-Quotes/imgs')
img=random.choice(files)
img = 'Marshall-Rosenberg-Quotes/imgs/' + img

api.update_with_media(img)
