import requests
from send_email import send_email


topic = "tesla"
api_key = "3df3c63c04f74334be38c9ec9b219495"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-12&sort" \
      "By=publishedAt&" \
      "apiKey=3df3c63c04f74334be38c9ec9b219495&" \
      "language=en"

# requests is the module of the library
# This requests.get(url) is the get requests for the http method
# This create the request object type
# All you get is a bunch of the code that is not readable at all
# This is getting the data from the following website: https://newsapi.org/

request = requests.get(url)
# Get the Dictionary using the json method
content = request.json()
# Access the article titles and the descriptions
body = ""
# It will keep iterating over the ['title'] and the ['description']
for article in content['articles'][:20]:
    # article['title'] here is referring to the
    # value associated with the key itself
    if article['title'] is not None:
        # Concatenation of the strings with another strings with 1 break and 2 break lines
        body = "Subject: Today news" + "\n" + body + article['title'] + "\n" + article["description"] + "\n" \
               + article['url'] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
