import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Enter your Spotify API credentials below
client_id = ''
client_secret = ''

def get_artist_top_tracks(artist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    top_tracks = sp.artist_top_tracks(artist_id)
    return top_tracks

def get_playlist_tracks(playlist_url):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    playlist_id = playlist_url.split('/')[-1]
    tracks = sp.playlist_tracks(playlist_id)['items']
    playlist_tracks = []
    for track in tracks:
        playlist_tracks.append(track['track']['name'])
    return playlist_tracks

def find_artist_top_songs_in_playlist(artist_id, playlist_url):
    artist_top_songs = get_artist_top_tracks(artist_id)
    playlist_tracks = get_playlist_tracks(playlist_url)
    occurrence_dict = {}
    for track in artist_top_songs['tracks']:
        if track['name'] in playlist_tracks:
            occurrence_dict[track['name']] = playlist_tracks.count(track['name'])
    if not occurrence_dict:
        print("Nenhuma música na playlist")
    else:
        print("Ocorrência das músicas do artista na playlist:")
        for song, occurrence in occurrence_dict.items():
            print(f"{song}: {occurrence}")

# Example usage:
playlist_url = "https://open.spotify.com/playlist/37i9dQZEVXbMXbN3EUUhlg"
artist_id = "3rfM2cGqF6DB0kUyytMkXx" 
find_artist_top_songs_in_playlist(artist_id, playlist_url)