#### This script successfully adds "#NVC #NonviolentCommunication" to any quotes shorter than 248 characters, with the least amount of formatting issues of anything else I could figure out so far. I had to do some manual editing to strip the unnecessary garbage that pyyaml adds to it.  Not a problem with multi-line editing.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, yaml

with open('hashquotes.yaml','r') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    quotes = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    new_quotes = []
    for quote in quotes:
        if len(quote) < 248:
           hashquote = quote + "\n\n#NVC #NonviolentCommunication"
           new_quotes.append(hashquote)
        else:
           new_quotes.append(quote)
with open('hashquote.yaml','w') as file:
    yaml.dump(new_quotes, file, default_style='\"', allow_unicode=True, explicit_start=True)
    file.close()
