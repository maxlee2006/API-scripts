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
#import main spotify link scraper
import playlistlinks

#API login
api = 'https://crushfm-staging.herokuapp.com/parse/login'


#login headers
headers = {
    'X-Parse-Application-Id': 'ID_HERE', 
    'X-Parse-Revocable-Session': 'XXX',
    'Content-Type': 'application/json'
}

#user credentials
user_credentials = {
    'username': 'USERNAME_HERE',
    'password': 'PASSWORD_HERE'
}

#get session token
def get_credentials():
     result = post(api, headers=headers, data = json.dumps(user_credentials))
     json_result = json.loads(result.content)
     token = json_result['sessionToken']
     return token

def get_headers_musicnerd(token):
     return {
         'X-Parse-Application-Id': 'APP_ID_HERE',
         'X-Parse-Session-Token': token,
         'Content-Type': 'application/json'
     }

def batchAddArtist(token, artist_url):
     url = f'https://crushfm-staging.herokuapp.com/parse/functions/batchAddArtist'
     addArtistData = {
          'urls': artist_url
     }
     addArtistHeaders = get_headers_musicnerd(token)
     result = post(url, headers=addArtistHeaders, data=json.dumps(addArtistData))
     json_result = json.loads(result.content)

     return(json_result)

def split_into_groups(lst, group_size):
    return [lst[i:i + group_size] for i in range(0, len(lst), group_size)]


playlistlinks


token = get_credentials()


artist_url = playlistlinks.artist_urls

linkGroups = split_into_groups(artist_url, 10)

for group in linkGroups:
     artist = batchAddArtist(token, group)
     print(json.dumps(artist))

#artist = addArtist(token, artist_url)


print(token)
