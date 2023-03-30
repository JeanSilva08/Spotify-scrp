import requests
from bs4 import BeautifulSoup
import csv

def get_artist_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the h1 tag with class "Type__TypeElement-sc-goli3j-0" and data-encore-id="type"
    h1_tag = soup.find("h1", {"class": "Type__TypeElement-sc-goli3j-0", "data-encore-id": "type"})

    # Get the text inside the h1 tag
    artist_name = h1_tag.text

    # Find the div tag with class "Type__TypeElement-sc-goli3j-0" and data-encore-id="type"
    div_tag = soup.find("div", {"class": "Type__TypeElement-sc-goli3j-0", "data-encore-id": "type"})

    # Get the text inside the div tag
    monthly_listeners = div_tag.text

    # Return the artist name and monthly listeners as a tuple
    return (artist_name, monthly_listeners.replace('ouvintes mensais', 'Ouvintes mensais'))


# Example usage
artists = [
    "https://open.spotify.com/artist/3rfM2cGqF6DB0kUyytMkXx", # Replace with artist 1 URL
    "https://open.spotify.com/artist/4yGgbQJMq9orWypwqtdzYT", # Replace with artist 2 URL
    "https://open.spotify.com/artist/28ie4NNTa2VW2QV4Zray8M", # Replace with artist 3 URL
    "https://open.spotify.com/artist/0BMccF4OSgl180EzdVFY9m", # Replace with artist 4 URL
    "https://open.spotify.com/artist/6jBww4kwlSrjaNYP7AQPtX", # Replace with artist 5 URL
    "https://open.spotify.com/artist/6J6U2JAv7LUF0cSQ98gpjM", # Replace with artist 6 URL
    "https://open.spotify.com/artist/2NMYOlZHIEsSq7pp5jBjic", # Replace with artist 7 URL
    "https://open.spotify.com/artist/2vWGxqWbGgmgxVDZ5CBvBP", # Replace with artist 8 URL
]


# Create a CSV file and write the header row
with open('artists.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Artist", "Monthly Listeners"])

    # Loop through each artist and write their information to the CSV file
    for artist_url in artists:
        artist_name, monthly_listeners = get_artist_info(artist_url)
        writer.writerow([artist_name, monthly_listeners])

print("Data exported to artists.csv")