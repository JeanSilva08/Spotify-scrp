import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

# Enter your Spotify API credentials below
client_id = ''
client_secret = ''

# Enter the artist names below
artist_names = ['Orochi', 'Mc Poze do Rodo', 'Oruam' , 'Raffé', 'Borges', 'PL Quest', 'Kizzy', 'Bielzin']

# Task 1: Get the number of followers for an artist

def get_followers(artist_name):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    results = sp.search(q=artist_name, type='artist')
    artist_id = results['artists']['items'][0]['id']
    num_followers = sp.artist(artist_id)['followers']['total']
    print(f'{artist_name} has {num_followers} followers on Spotify.')
    return num_followers

# Task 2: Get the popularity of an artist

def get_popularity(artist_name):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    results = sp.search(q=artist_name, type='artist')
    artist_id = results['artists']['items'][0]['id']
    popularity = sp.artist(artist_id)['popularity']
    print(f'{artist_name} has a popularity score of {popularity} on Spotify.')
    return popularity

# Task 3: Export the data to a CSV file

def export_data(artist_name, num_followers, popularity, first_time):
    with open('artists_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if first_time:
            writer.writerow(['Artista', 'Número de seguidores', 'Pontos de Popularidade'])
        writer.writerow([artist_name, num_followers, popularity])
    print(f'The data for {artist_name} has been exported to artists_data.csv.')

if __name__ == '__main__':
    first_time = True
    for artist_name in artist_names:
        num_followers = get_followers(artist_name)
        popularity = get_popularity(artist_name)
        export_data(artist_name, num_followers, popularity, first_time)
        first_time = False
