import requests
import streamlit as st

# Prepare API key and API url
api_key = "Use your own API"
# https://api.nasa.gov/
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data in the form of the dictionary
response1 = requests.get(url)

data = response1.json()

# Extract the image title, url and, explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image and the image filepath would be "img.png"
image_filepath = "img.png"
response2 = requests.get(image_url)
# This will create the image itself
with open(image_filepath, 'wb') as file:
    file.write(response2.content)


# This will create the title,
# image and the text respectively:
st.title(title)
st.image(image_filepath)
st.write(explanation)


# Things to note:
# Please change the part after "apiKey=" to reflect your own API which
# you will get from newsapi.org after creating a free account there.
# https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=890603a55bfa47048e4490069ebee18c





