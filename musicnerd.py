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

#API login
api = 'https://crushfm-staging.herokuapp.com/parse/login'


#login headers
headers = {
    'X-Parse-Application-Id': 'APP_ID_HERE',
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

def addArtist(token, artist_url):
     url = f'https://crushfm-staging.herokuapp.com/parse/functions/addArtist'
     addArtistData = {
          'url': artist_url
     }
     addArtistHeaders = get_headers_musicnerd(token)
     result = post(url, headers=addArtistHeaders, data=json.dumps(addArtistData))
     json_result = json.loads(result.content)

     return(json_result)




token = get_credentials()

artist_url = "https://open.spotify.com/artist/4mAOWQpb5gJLsHP2hCkVm5?si=2b772081ba79465a"

artist = addArtist(token, artist_url)


print(token)
print(artist)
print(json.dumps(artist_url))