A bundle of scripts that communicate with Spotify and Google web APIs.

!! REQUIRES SPOTIFY API CLIENT ID AND SECRET !!

!! MUSICNERD FILES REQUIRE ID AND API KEY !!

--FILE LIST--

google.py: interfaces with google's custom search API to get links for certain social medias based on user's input

instagram.py: similar to google.py, but uses BeautifulSoup as a webscraper instead of google's API

links.py: no longer works, but is similar to instagram.py

musicnerdBatchAddArtist.py: a program that interfaces with MusicNerd's API and adds all artists from a playlist into their database. Doesn't work well when a song has more than one artist (interfaces with playlistlinks.py)

musicnerd.py: similar to BatchAddArtist, but only adds a single artist not based on user input

playlistlinks.py: asks user to input a playlist link from spotify, trims the link down and returns a list of the tracks and spotify links to the artists

playlists.py: like playlistlinks.py, but allows the user to rerun the script

