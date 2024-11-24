import requests

def search_google_custom_api(query, api_key, cse_id):
    # Construct the search URL
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id
    }
    
    # Perform the HTTP GET request
    response = requests.get(url, params=params)
    
    # Check for request errors
    response.raise_for_status()
    
    # Parse the response JSON
    data = response.json()
    links = []
    
    # Extract the URLs from the search results
    for item in data.get('items', []):
        link = item.get('link')
        links.append(link)
    
    return links

# Define your API Key and Custom Search Engine ID
API_KEY = ''  # Replace with your actual API key!
CSE_ID = ''    # Replace with your actual Custom Search Engine ID!

# Define domains for different social media platforms
domains = {
    'linktree': 'linktr.ee',
    'twitter': 'x.com',
    'youtube': 'youtube.com/channel',
    'bandcamp': 'bandcamp.com',
    'facebook': 'facebook.com',
    'tiktok': 'tiktok.com',
    'instagram': 'instagram.com',
    'bandsintown': 'bandsintown.com',
    'twitch': 'twitch.tv'
}

# Example query
query = input("Enter the name of the artist you'd like to search for: ")

# Search for each domain
for platform, domain in domains.items():
    search_query = f"{query} site:{domain}"
    print(f"\n{platform.capitalize()} Links for '{query}':")
    try:
        social_media_links = search_google_custom_api(search_query, API_KEY, CSE_ID)
        if social_media_links:
            for link in social_media_links:
                print(link)
        else:
            print(f"No {platform} links found.")
    except requests.exceptions.RequestException as e:
        print(f"Error searching {platform}: {e}")