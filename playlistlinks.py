#This script will grab an authorization token from Spotify's API using environment variables, and perform a basic query for playlist tracks and artists based on a spotify link.

#DOTENV needed to read environment variables from .env file
from dotenv import load_dotenv
#os to interact with .env file
import os
#base64 for encoding 
import base64
#allows program to send a post and get request
from requests import post, get
#json needed to parse query data and convert to python dict
import json
#import spotify playlist reader


#load environment variables
load_dotenv()

#set environment variables to variables in main file
client_id = os.getenv("CLIENT_ID") #SPOTIFY ID
client_secret = os.getenv("CLIENT_SECRET") #SPOTIFY SECRET


#grab token from API using client_id and client_secret
def get_token():
    #set authentication string
    auth_string = client_id + ":" + client_secret
    #encode authentication string
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    #retrieve token
    url = "https://accounts.spotify.com/api/token"
    #send and format data so Spotify API can understand
    headers = {
        #Authorization level is set at "Basic"
        "Authorization": "Basic " + auth_base64,
        #Specify content type
        "Content-Type": "application/x-www-form-urlencoded"

    }
    #API requires program to pass a grant type
    data = {"grant_type": "client_credentials"}
    #format all data and send a post to the API
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    
    #Returns an access token
    return token

#Creates authorization header for convenience, otherwise we would have to declare authorization for each query
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

#This function queries for an artist based on user input but is not being used in the program
# def search_for_artists(token, artist_name):
#     url = "https://api.spotify.com/v1/search"
#     headers = get_auth_header(token)
#     query = f"?q={artist_name}&type=artist&limit=1"

#     query_url = url + query
#     result = get(query_url, headers=headers)
#     json_result = json.loads(result.content)

#     return json_result

#This function queries for a playlist based on the playlist ID present in a spotify link and returns a .json of track data on each song in the playlist
def search_for_playlists(token, playlist_id):
    ##Create search URL, varies based on what you want to query for
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    #Get authentication headers using a function made earlier
    headers = get_auth_header(token)
    #grab data from API
    result = get(url, headers=headers)
    #check if return is valid, if not send an error and stop the program
    result.raise_for_status()
    #convert .json into format that can be parsed by python
    json_result = json.loads(result.content)["items"]
    #return praseable data
    return json_result

#This is the "frontend" of the program that dictates the user experience

#while loop that keeps program constantly running unless told to stop
runScript = True


#get token using function
token = get_token()

#intro text
print("Welcome! This program will find the artist links of the first 100 tracks in a playlist. Your user token is: " + token)

#user input
playlist_link = input("enter your playlist link here: ")


    
#trim down spotify link to just the ID

playlist_id = playlist_link.strip("https://open.spotify.com/playlist/")
playlist_id = playlist_id.split("?")[0]


    
    #query for playlist using function 
tracks = search_for_playlists(token, playlist_id)

artist_urls = []

    #list track name and artist's spotify link from queried data
for idx, track_item in enumerate(tracks):
    track = track_item['track']
    # Get artist URLs as a flat list
    artist_links = [artist['external_urls']['spotify'] for artist in track['artists']]
    artist_urls.extend(artist_links)  # Append the URLs to the main list
    print(f"{idx + 1}. Track: {track['name']}")
    print(f"   Links: {', '.join(artist_links)}") 









