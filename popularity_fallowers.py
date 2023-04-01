import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

# Enter your Spotify API credentials below
client_id = ''
client_secret = ''

# Enter the artist names below
artist_names = ['L7nnon', 'Xamã', 'WIU' , 'MC Cabelinho', 'Orochi', 'Neobeats', 'Teto', 'Matuê', 'Oruam', 'Pineapple Storm', 'Mainstreet', 'Felipe Ret', 'Chefin', 'Salve Malak', 'TZ da Coronel', 'Ajaxx', 'Dallas', 'Chris MC', 'MC Poze', 'Bin', 'Mello', 'Vulgo FK', 'Delacruz', 'Hungria', 'Djonga ', 'N.I.N.A', 'Borges', 'Nagalli', 'Baco Exu do Blues', 'BK', 'Caio Luccas', 'Galdino', 'PK', 'Caio Passos', 'DJ Matt D', 'Victor Wao', 'Azzy', 'DJ Gustah', 'AMUSIK', 'Menor MC', 'Emicida', 'Lourena', 'Bielzin', 'Supernova Ent.', 'Medellin', 'Kweller', 'Luiz Lins', 'Kawe', 'Pedro Lotto', 'MãoLee', 'Coyote Beatz', 'Skeeter Beats', 'MD Chefe ', '1KILO', 'Cynthia Luz', 'Luccas Carlos', 'Tropkillaz', 'Marcelo D2', 'Nada Mal', 'Projota ', 'Papatinho', 'Jess Beats', 'Costa Gold', 'Negra Li', 'Froid', 'César MC', 'Sidoka', 'Dfideliz', 'Malibu Studios', 'Budah', 'Chris Beats ZN', 'Kizzy', 'OQ Produções', 'Jaya Luck', 'PL Quest', 'WC no Beat', 'Raffé', 'CalliCartel', 'Orgânico', 'Leviano', 'Hash Produções', 'Uclã Records', 'Altamira TV', 'André Nine', 'Rashid', 'Clau', 'WEY', 'Rock Danger', 'Karol Conka', 'Offlei Sounds', 'Black', 'Flora matos ', 'Aldeia Records', 'Isso que é som de RAP', 'Mvk', 'A Banca Records', 'Paiva Prod', 'Alaska', 'Pior versão de mim ', 'Shenlong', 'Distrito 23', 'Tropa do Bruxo', 'Buddy Poke ', 'Ebony', 'Drik Barbosa', 'LP Beatzz', 'MC Filhão ', 'Clara Lima', 'Feek', 'Intactoz Corp.', 'Elenko Music', 'Hashi', 'Oreozin', 'CMK', '7Minutoz', 'Oliveira']

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
            writer.writerow(['Artista', 'Seguidores', 'Popularidade 0-100'])
        writer.writerow([artist_name, num_followers, popularity])
    print(f'The data for {artist_name} has been exported to artists_data.csv.')

if __name__ == '__main__':
    first_time = True
    for artist_name in artist_names:
        num_followers = get_followers(artist_name)
        popularity = get_popularity(artist_name)
        export_data(artist_name, num_followers, popularity, first_time)
        first_time = False
