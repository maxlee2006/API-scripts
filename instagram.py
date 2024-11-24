import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_instagram(query):
    # Encode the query to be URL-safe and construct the search URL
    search_query = urllib.parse.quote_plus(query + " site:instagram.com")
    url = f"https://www.google.com/search?q={search_query}"
    
    # Headers to mimic a browser request!
    headers = {
        "User-Agent": "Safari/537.36"
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
            # Check if the link contains 'instagram.com'
            if 'instagram.com' in link:
                if 'maps.google.com' in link or 'accounts.google.com' in link or 'search%' in link:
                    continue

                else:
                    links.append(link)

    
    return links

def search_linktree(query):
    # Encode the query to be URL-safe and construct the search URL
    search_query = urllib.parse.quote_plus(query + " site:linktr.ee")
    url = f"https://www.google.com/search?q={search_query}"
    
    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Safari/537.36"
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
            # Check if the link contains 'instagram.com'
            if 'linktr.ee' in link:
                if 'maps.google.com' in link or 'accounts.google.com' in link or 'search%' in link:
                    continue

                else:
                    links.append(link)
    
    return links

# Example search query
query = input("Type the name of an artist to research: ")
instagram_links = search_instagram(query)
linktree = search_linktree(query)

print(f"Instagram Links for '{query}':")
if instagram_links:
    for link in instagram_links:
        print(link)
else:
    print("No Instagram links found.")

print(f"Linktree links for '{query}':")
if linktree:
    for link in linktree:
        print(link)
else:
    print("No Linktree links found.")