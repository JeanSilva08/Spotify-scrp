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
    return (artist_name, monthly_listeners.replace('monthly listeners', 'Ouvintes mensais'))


# Example usage
artists = [
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
    "https://open.spotify.com/artist/28ie4NNTa2VW2QV4Zray8M",
    "https://open.spotify.com/artist/1WXbiUMl1AT9Inb619xPUg",
    "https://open.spotify.com/artist/5e9fQ7H6ynkMPiZM2ADQDm",
    "https://open.spotify.com/artist/27azwwkxutWL1BWMkgNIh0",
    "https://open.spotify.com/artist/1MzXJ8AaHdidMAnjgcahS4",
    "https://open.spotify.com/artist/0vLuOi2k62sHujIfplInlK",
    "https://open.spotify.com/artist/204IwDdaHE4ymGk9Kya2pY",
    "https://open.spotify.com/artist/32NfHH4nSmu97Z4RQjPyET",
    "https://open.spotify.com/artist/6jBww4kwlSrjaNYP7AQPtX",
    "https://open.spotify.com/artist/6TPJK8tv3AKKSsw0lENTQk",
    "https://open.spotify.com/artist/78nr1pVnDR7qZH6QbVMYZf",
    "https://open.spotify.com/artist/1YOVBTvznjiDvtAj4ExHeo",
    "https://open.spotify.com/artist/1a3fr7NdeBT4JlGj6YlbDL",
    "https://open.spotify.com/artist/0WvTL8PecsD3VxRGuHdSxj",
    "https://open.spotify.com/artist/5xYkM2vMrE23taj6tl7qkm",
    "https://open.spotify.com/artist/6zGPa2tLMJ5HQYUddZI8di",
    "https://open.spotify.com/artist/1rIc4yTieeRq25NA3T8RQ5",
    "https://open.spotify.com/artist/1ew4rMO5r0Oon1R9xZxo8Q",
    "https://open.spotify.com/artist/1uf8uSErmKc3JVtmjVBZ83",
    "https://open.spotify.com/artist/0nzfP49X2nrzmmkwZf180L",
    "https://open.spotify.com/artist/48r1nXoaPXPSx1LoM0Rnzl",
    "https://open.spotify.com/artist/78Y1NpgD0yMKoBetaYlUzS",
    "https://open.spotify.com/artist/2d9LRvQJnAXRijqIJDDs2K",
    "https://open.spotify.com/artist/3jLj1sAQaEpLpktyJmyGIh",
    "https://open.spotify.com/artist/2vWGxqWbGgmgxVDZ5CBvBP",
    "https://open.spotify.com/artist/3prRKGJz16RRMRSIM97nHw",
    "https://open.spotify.com/artist/06zC1Z0YDLeWPBLIEAkswh",
    "https://open.spotify.com/artist/4W4NkfM4A1sX2S2bfYlV07",
    "https://open.spotify.com/artist/0hWRVPGWjaXcEvg8l65Tx0",
    "https://open.spotify.com/artist/1TYJOhNSxMOODWiDVhuyZb",
    "https://open.spotify.com/artist/23ot0eI6ByBW6LrlBfr2bm",
    "https://open.spotify.com/artist/72aE07MxpePfCELo4vGZcK",
    "https://open.spotify.com/artist/2PhFsxtwCQLS3e9SJwDN3j",
    "https://open.spotify.com/artist/42xf1iqSOZluDWJ8RW2B9H",
    "https://open.spotify.com/artist/6yZKPB8eRoJesHjtxPxSLs",
    "https://open.spotify.com/artist/6E2st8OqIaS7PU5gj95FSE",
    "https://open.spotify.com/artist/0QHGCPmM4UgeNvrNPntSlu",
    "https://open.spotify.com/artist/5WFFFHVqeVk5tLuYh2KjQy",
    "https://open.spotify.com/artist/5bzWtCkjIAMgN93gLt56SO",
    "https://open.spotify.com/artist/1vEN3d3dJbmdHQpXD6AIkL",
    "https://open.spotify.com/artist/3YVxmhkewoRHu8WFgWlCb7",
    "https://open.spotify.com/artist/2zGf6lwQ9PxXdoeo5XXP2K",
    "https://open.spotify.com/artist/0iZz25uH5PLaShpqq84uYv",
    "https://open.spotify.com/artist/7uskxjQtkzfiqHCNIIv3gD",
    "https://open.spotify.com/artist/7q1aEytv83jXNECmyaMhgn",
    "https://open.spotify.com/artist/1E4r5qziZja6v8jA7iTqjn",
    "https://open.spotify.com/artist/45Yz90pqjzEdJzpEQg1eII",
    "https://open.spotify.com/artist/19JY4BpaJkAlSR4iDxB1MX",
    "https://open.spotify.com/artist/7EyzyrMNgqiK8bMrbkOT9l",
    "https://open.spotify.com/artist/0oNOkdVXXFaWC9tPb7Ol10",
    "https://open.spotify.com/artist/0PMk31f9Log4ixwUUY40p6",
    "https://open.spotify.com/artist/08zSkHjCY3ypH4gdBVHWgO",
    "https://open.spotify.com/artist/0YOr5sV4zMMyj5xviWiFjW",
    "https://open.spotify.com/artist/2NMYOlZHIEsSq7pp5jBjic",
    "https://open.spotify.com/artist/5ZTnWo7IY6rdIxm6aTSR84",
    "https://open.spotify.com/artist/4oxFgud0qa3A1tE6JFpFVp",
    "https://open.spotify.com/artist/6J6U2JAv7LUF0cSQ98gpjM",
    "https://open.spotify.com/artist/2QjS2N6sORI7H4qbf6xitS",
    "https://open.spotify.com/artist/0BMccF4OSgl180EzdVFY9m",
    "https://open.spotify.com/artist/0s5MMDYKWYf4XksClf5Oiq",
    "https://open.spotify.com/artist/5UOOgRWguRmVZo1voJuQpf",
    "https://open.spotify.com/artist/0xEdwBYYjxw6wk179Tq2sJ",
    "https://open.spotify.com/artist/4BZ0ACrHCLropCpHJypPvV",
    "https://open.spotify.com/artist/4zP89WNloauEX8v8JdZbxP",
    "https://open.spotify.com/artist/12xPPAGu03vdZR3AmWNIxZ",
    "https://open.spotify.com/artist/5cc7XCY3YdVmFDYw9LklMq",
    "https://open.spotify.com/artist/5WgRuO0mhM36NFoapzpWBH",
    "https://open.spotify.com/artist/13A9x5VINTOaVnYxK4rbNQ",
    "https://open.spotify.com/artist/6nZ39vMOOOgXQ471Jy5jhR",
    "https://open.spotify.com/artist/1mjuRRMumbLmGmHmYvMDcb",
    "https://open.spotify.com/artist/6ODCVWBfGNFUf1bpo0c2Ge",
    "https://open.spotify.com/artist/7Kqcr4CkcQHjHiw3aPfFkC",
    "https://open.spotify.com/artist/0oNOkdVXXFaWC9tPb7Ol10",
    "https://open.spotify.com/artist/5Znx4PG5UsUitigaJnmZX3",
    "https://open.spotify.com/artist/5q9yc7RScObCN016xvstXM",
    "https://open.spotify.com/artist/43DrL9cHm49HEwg85idE2c",
    "https://open.spotify.com/artist/78TUxGXS6Jpos6nj2oEqSP",
    "https://open.spotify.com/artist/0Do6bAo2kcVLp7ekzypskJ",
    "https://open.spotify.com/artist/1T0F05F7TEo6QYr4vtGJdb",
    "https://open.spotify.com/artist/1D8yVlgOfpn6lW5UfwOMj7",
    "https://open.spotify.com/artist/3VI6PCewAVll6K4cYoNWt7",
    "https://open.spotify.com/artist/6Dzh6uXgA0QKVg1eIWxdDY",
    "https://open.spotify.com/artist/5itNRAG8DPcD6Yrm1rFPLv",
    "https://open.spotify.com/artist/4s3lxX76LwxzMdQEAFYdzv",
    "https://open.spotify.com/artist/5OQwCMHaNZ6FtVcVNkkShY",
    "https://open.spotify.com/artist/1UBSRfDGNkhpTWQeMyCwHb",
    "https://open.spotify.com/artist/1VJZvjGu80pBwk0qeJz8ZR",
    "https://open.spotify.com/artist/3WFKRRXUORuPPdH11Spele",
    "https://open.spotify.com/artist/0bRPXWabRuRy4RqnycT5ne",
    "https://open.spotify.com/artist/4XdUyu7YX6zgKLi34JYQSG",
    "https://open.spotify.com/artist/7rVT3dNwCamCtw5rC7salV",
    "https://open.spotify.com/artist/3uMHwSzAIRTT0pRMihvQJw",
    "https://open.spotify.com/artist/6OAAuXhPzzofYSaiIGHasL",
    "https://open.spotify.com/artist/137b3EpKbbmxmY2dGgzx2Q",
    "https://open.spotify.com/artist/6MWb3O5RfehDbCZsBfGrIG",
    "https://open.spotify.com/artist/6QmnOxsr8M6iD5Zqpb2src",
    "https://open.spotify.com/artist/2563ILWHSx52eOxOoi5rJW",
    "https://open.spotify.com/artist/65ZE0dYy4XIHtFBAGMKHhI",
    
        
]


# Create a CSV file and write the header row
with open('artists.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Artista", "Ouvintes Mensais"])

    # Loop through each artist and write their information to the CSV file
    for artist_url in artists:
        artist_name, monthly_listeners = get_artist_info(artist_url)
        writer.writerow([artist_name, monthly_listeners])

print("Data exported to artists.csv")