import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

client_id = ''
client_secret = ''

# prompt the user to enter the playlist URL
playlist_url = input("Enter the playlist URL: ")
 
# list of artist URLs
artist_urls = [
    "https://open.spotify.com/artist/0JjPiLQNgAFaEkwoy56B1C",
    "https://open.spotify.com/artist/5YwzDz4RJfTiMHS4tdR5Lf",
    "https://open.spotify.com/artist/3MrDVzg7ZXaYMyQmbDInr7",
    "https://open.spotify.com/artist/1WQBwwssN6r8DSjUlkyUGW",
    "https://open.spotify.com/artist/3rfM2cGqF6DB0kUyytMkXx",
    "https://open.spotify.com/artist/6PERJZF7wohA034PAxDK0b",
    "https://open.spotify.com/artist/68YeXpLt3jB7JHQS5ZjMGo",
    "https://open.spotify.com/artist/5nP8x4uEFjAAmDzwOEc9b8",
    "https://open.spotify.com/artist/4yGgbQJMq9orWypwqtdzYT",
    "https://open.spotify.com/artist/09U6hmCerKcIJrixubiBjm",
    "https://open.spotify.com/artist/25XJqeReVV38w0tR04GGBd",
    "https://open.spotify.com/artist/7gJN8W0589FisSYJS17K54",
    "https://open.spotify.com/artist/68PYmgkbRP1qZnEWOry7sB",
    "https://open.spotify.com/artist/7zxFc10N9BP2lg73b8cwZ0",
    "https://open.spotify.com/artist/3lIU3RoZiHen1QXAQ3KQ9e",
    "https://open.spotify.com/artist/0y7B2G0jNMGWyQJsOoRMUt",
    "https://open.spotify.com/artist/4LAFtDzlQM89xov636hMVv",
    "https://open.spotify.com/artist/0obu7Om4zu9ahul5DI4JtY",
    ]

# authenticate with Spotify Web API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

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

# check if the artists are in any of the tracks
rows = []
artist_names = []
for artist_url in artist_urls:
    # get the artist name and ID from the API
    artist_id = sp.artist(artist_url)['id']
    artist_name = sp.artist(artist_url)['name']
    artist_names.append(artist_name)
    
    for i, track in enumerate(playlist_tracks):
        # get the track details from the API
        track_id = track['track']['id']
        track_details = sp.track(track_id)

        # check if the artist is in the track artist list
        for track_artist in track_details['artists']:
            if track_artist['id'] == artist_id:
                position = i+1
                rows.append([position, track_details['name'], artist_name])
                print(f"{artist_name} has a track in the playlist {playlist_url}: {position}. {track_details['name']}")
                break
            elif ' featuring ' in track_details['name'].lower():
                # check if the artist is featured in the track
                if artist_id in [feat['id'] for feat in track_details['artists']]:
                    position = i+1
                    rows.append([position, track_details['name'], artist_name])
                    print(f"{artist_name} has a featured track in the playlist {playlist_url}: {position}. {track_details['name']}")
                    break

# write the results to a CSV file
filename = f"{'_'.join(artist_names)}_in_{playlist_id}.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Position', 'Track Name', 'Artist Name'])
    for row in rows:
        writer.writerow(row)

print(f"The results have been saved to {filename}")