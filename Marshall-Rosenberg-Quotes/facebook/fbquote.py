import facebook, yaml, random, os

page_access_token = os.environ.get('page_access_token')
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "101805031688301"

with open('Marshall-Rosenberg-Quotes/quotebot/quotes.yaml','r') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    quotes = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    item = random.choice(quotes)
    graph.put_object(facebook_page_id, "feed", message=item)

