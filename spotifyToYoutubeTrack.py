import os
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import youtube_dl as yt
from youtube_search import YoutubeSearch

scope = "user-library-read"

_list ="SPOTIFY TRACK"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='CLIENT ID',client_secret='CLIENT SECRET'))
results = sp.track(_list)
_song = results['name']
_uri = results['uri']
_songArtist = sp.track(_uri)
_Artist = _songArtist['artists']
_jsonPart = json.dumps(_Artist)
_findArtist = sp.artist(_jsonPart[32:86])
_youtubeArtist = _findArtist['name']
results1 = YoutubeSearch(f'{_song} {_youtubeArtist}', max_results=1).to_json()
_youtubeSearch= results1.split(':')
_myLinkLast = _youtubeSearch[len(_youtubeSearch)-1].replace('"}]}','')
_myLinkStart = _myLinkLast.replace('"/','')
print(_myLinkStart)
