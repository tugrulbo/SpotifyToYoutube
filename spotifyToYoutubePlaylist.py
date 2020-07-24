import os
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import youtube_dl as yt
from youtube_search import YoutubeSearch

songs = []

scope = "user-library-read"

_track ="SPOTIFY LIST"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='CLIENT ID',client_secret='CLIENT SECRET'))
results = sp.playlist(_track)
_queues=[]
_listOfTracks=[]
newResults=sp.playlist_tracks(_track)
x=0
tracks = newResults['items'] 
for x in range(len(tracks)):
    _listOfTracks.append(tracks[x]['track']['external_urls']['spotify'])
    results = sp.track(_listOfTracks[x])
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
    _spaceCheck = _myLinkStart.strip()
    _youtubeLink = f"https://www.youtube.com/{_spaceCheck}"
    _queues.append(_youtubeLink)

print(_queues)
