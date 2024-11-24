import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
import random

def search_social_media(query, domain):
    # Encode the query to be URL-safe and construct the search URL!
    search_query = urllib.parse.quote_plus(query + f" site:{domain}")
    url = f"https://www.google.com/search?q={search_query}"
    
    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Chrome/92.0.4615.107"
    }
    
    # Perform the HTTP GET request
    response = requests.get(url, headers=headers)
    
    # Check for request errors
    response.raise_for_status()
    
    # Parse the response HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all links in the search result
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        # Look for Google search result links which are typically prefixed with '/url?q='
        if '/url?q=' in href:
            # Extract the actual URL
            link = href.split('/url?q=')[1].split('&')[0]
            # Check if the link contains the specified domain
            if domain in link:
                # Filter out unwanted links
                if any(subdomain in link for subdomain in ['maps.google.com', 'accounts.google.com', 'search%']):
                    continue
                links.append(link)
        time.sleep(random(1, 3))
    
    return links

# Define domains for different social media platforms
domains = {
    'linktree' : 'linktr.ee',
    'twitter': 'x.com',
    'youtube': 'youtube.com/channel',
    'bandcamp': 'bandcamp.com',
    'facebook': 'facebook.com',
    'tiktok' : 'tiktok.com',
    'instagram': 'instagram.com'
}

# Example query
query = input("enter the name of the artist you'd like to search for: ")

# Search for each domain
for platform, domain in domains.items():
    print(f"\n{platform.capitalize()} Links for '{query}':")
    social_media_links = search_social_media(query, domain)
    if social_media_links:
        for link in social_media_links:
            print(link)
    else:
        print(f"No {platform} links found.")