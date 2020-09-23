#!/usr/bin/env python
# -*- coding: utf-8 -*-
import facebook, yaml, random, os

page_access_token = os.environ.get('page_access_token')

graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "101805031688301"

files=os.listdir('Marshall-Rosenberg-Quotes/imgs/')
img = 'Marshall-Rosenberg-Quotes/imgs/' + random.choice(files)
photo = open(img, "rb").read()

graph.put_photo(image=photo, parent_object=facebook_page_id)


