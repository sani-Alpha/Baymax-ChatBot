#!/usr/bin/python3
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import webbrowser
from  textblob import TextBlob
import random
import cgi

form3 = cgi.FieldStorage()
string = form3.getvalue("text")

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of header

client_id="bb592cc71fbf46ba83c57b311f9e0c7d"
client_secret="74fa7053d85449bcadc234693b065821"

client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

analysis=TextBlob(string)
polar=analysis.sentiment.polarity
#analysis.sentiment
#print(polar)
genres=""
if polar>=-1.0 and polar<-0.5:
  print("You should let you feelings out and listen to some metal\n Here is the link")
  genres=['hip-hop','metal']
elif polar>=-0.5 and polar<0:
  print("piano and acoustic music is best as i think you are sad.\nHere is the link")
  genres=['piano','acoustic']
elif polar>0 and polar<0.5:
  print("Let me play some soothing music for you to fall sleep.\n Here is the link")
  genres=['classical','jazz']
else:
  print("Let me play some pop music for you just to set the mood.\n Here is the link")
  genres=['pop','edm','breakbeat','electro']

song=sp.recommendations(seed_genres=genres)

song_url=song["tracks"][random.randint(1,5)]["artists"][0]['external_urls']["spotify"]
song_url=song_url.replace("artist","embed/artist")
print('<iframe src="'+song_url+'" width="300" height="380" frameborder="0" allowtransparency="true" allow="autoplay"></iframe>')

