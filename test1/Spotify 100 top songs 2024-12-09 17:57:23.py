# Databricks notebook source

!pip install spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# COMMAND ----------

import spotipy
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
from time import sleep
from datetime import date, timedelta

# COMMAND ----------

client_id='292240685061457192c80564e4b29791'
client_secret='b1b20d93c32a4c6bb66aecdc8b902cd0'

# COMMAND ----------

#Authentication - without user
client_credentials_manager_token = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager_token)


# COMMAND ----------

top_100_track = sp.playlist_tracks('5ABHKGoOzxkaa28ttQV9sE')

# COMMAND ----------

top_100_track.keys()

# COMMAND ----------

top_100_track['items'][0].keys()

# COMMAND ----------

tracks = top_100_track['items'][99]

# COMMAND ----------

tracks.keys()

# COMMAND ----------

tracks['track'].keys()

# COMMAND ----------

type =[]
track=[]
release_date=[]
album_type=[]
available_markets=[]
artists =[]
disc_number =[]
track_number = []
duration_ms = []
name =[]
popularity = []
is_social = []

# COMMAND ----------

[item['track']['album'].keys() for item in top_100_track['items']]

# COMMAND ----------


for i in top_100_track['items']:
    type.append(i['track']['type'])
    track.append(i['track']['track'])
    release_date.append(i['track']['album']['release_date'])
    album_type.append(i['track']['album']['album_type'])
    available_markets.append(i['track']['album']['available_markets'])
    artists.append([artist['name'] for artist in i['track']['artists']])
    disc_number.append(i['track']['disc_number'])
    track_number.append(i['track']['track_number'])
    duration_ms.append(i['track']['duration_ms'])
    name.append(i['track']['name'])
    popularity.append(i['track']['popularity'])

# COMMAND ----------

print(len(popularity),
len(type))

# COMMAND ----------

df = pd.DataFrame({'popularity': popularity, 'type': type, 'track': track, 'album_type': album_type, 'release_date': release_date, 'available_markets': available_markets, 'artists': artists, 'disc_number': disc_number, 'track_number': track_number, 'duration_ms': duration_ms, 'name': name})

# COMMAND ----------

df
