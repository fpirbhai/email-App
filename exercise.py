import requests
import streamlit as st

API_KEY = 'fm8kW9bWzFexHoyiadPkmf8qZbTvGqn5dWGr7sjT'
URL = 'https://api.nasa.gov/planetary/apod?api_key=fm8kW9bWzFexHoyiadPkmf8qZbTvGqn5dWGr7sjT'

response = requests.get(url=URL,verify=False)

data = response.json()

url_pix = data['url']
title = data['title']
description = data['explanation']
print(url_pix)

pix = requests.get(url_pix, verify=False)

# print(pix.content)

st.set_page_config(page_title='NASA APOD', layout='wide')

st.title('NASA Astronomy Pic of the Day')

with open("picture.jpeg", "wb") as pic:
    pic.write(pix.content)

st.image(image='picture.jpeg', width=460)

st.write(description)