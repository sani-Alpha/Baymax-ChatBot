#!/usr/bin/python3
# coding: utf-8

# In[1]:


import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import webbrowser
import cgi

import nltk
from  textblob import TextBlob
from  nltk.stem  import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize


# In[2]:
form3 = cgi.FieldStorage()
string = form3.getvalue("text")

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers


search_str="kids"

client_id="bb592cc71fbf46ba83c57b311f9e0c7d"
client_secret="74fa7053d85449bcadc234693b065821"

client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
result=sp.search("Happier")
#print(result)
url=result["tracks"]["items"][0]["artists"][0]["external_urls"]["spotify"]
url_id=result["tracks"]["items"][0]["artists"][0]["id"]
artist=sp.artist(artist_id=url_id)
artists_songs=sp.artist_top_tracks(artist_id=url_id,country='US')
#pprint.pprint(artists_songs)
#webbrowser.open_new_tab()


# In[3]:


analysis=TextBlob(string)
sentiments=analysis.sentiment.polarity
genres=''
if sentiments <= -.1 and sentiments > -.2:
    print("I think you should listen folk.")
    genres='roots'
elif sentiments >=.1 and sentiments <.2:
    print("I think you should listen chill ")
    genres='chill'
elif sentiments >=.2 and sentiments <.3:
    print("I think you should listen indian ")
    genres='indian'
elif sentiments <=-.2 and sentiments >-.3:
    print("I think you should listen classical ")
    genres='classical'
elif sentiments >=.6 and sentiments <.8:
    print("I think you should listen dance ")
    genres='party'
elif sentiments <=-.6 and sentiments >-.8:
    print("I think you should listen romance")
    genres='romance'
elif sentiments >=.4 and sentiments <.6:
    print("I think you should listen happy ")
    genres='happy'
elif sentiments <.4 and sentiments >=.3:
    print("I think you should listen hip-hop ")
    genres='hip-hop'
elif sentiments >=.8 and sentiments <1.0:
    print("I think you should listen disco music ")
    genres='disco'
elif sentiments >-0.1 and sentiments <=0.1:
    print("I think you should listen dubstep music,\n Here is the link:"+url+"")
    genres='dubstep'

