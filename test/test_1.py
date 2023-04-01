import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = ''
client_secret = ''

# prompt the user to enter the artist and playlist URLs
artist_url = input("Enter the artist URL: ")
playlist_url = input("Enter the playlist URL: ")

# authenticate with Spotify Web API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# get the artist ID from the API
artist_id = sp.artist(artist_url)['id']

# get the playlist ID from the API
playlist_id = playlist_url.split('/')[-1]

# get the tracks from the playlist
playlist_tracks = []
offset = 0
while True:
    tracks = sp.playlist_tracks(playlist_id, offset=offset)
    playlist_tracks.extend(tracks['items'])
    offset += len(tracks['items'])
    if not tracks['next']:
        break

# check if the artist is in any of the tracks
for track in playlist_tracks:
    # get the track details from the API
    track_id = track['track']['id']
    track_details = sp.track(track_id)

    # check if the artist is in the track artist list
    for track_artist in track_details['artists']:
        if track_artist['id'] == artist_id:
            print(f"{artist_url} has a track in the playlist {playlist_url}: {track_details['name']}")
            break
        elif ' featuring ' in track_details['name'].lower():
            # check if the artist is featured in the track
            if artist_id in [feat['id'] for feat in track_details['artists']]:
                print(f"{artist_url} has a featured track in the playlist {playlist_url}: {track_details['name']}")
                break
