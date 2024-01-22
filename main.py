import requests
from bs4 import BeautifulSoup
import json
from collections import Counter

# Define the search query
search_query = "Minecraft server hosting"

# Define the number of pages to scrape
num_pages = 10

# Create a list to store the results
results = []

# Create a counter to track the number of results found
keywords = Counter()

# Set the headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

# Loop through each page of search results
for page_num in range(1, num_pages + 1):
    url = f"https://www.google.com/search?q={search_query}&start={(page_num - 1) * 10}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all("div", class_="g")
    
    # Get the title and description of the search result in a loop
    for result in search_results:
        title_element = result.find("h3")
        title = title_element.text if title_element else "No title found"
        description_element = result.find("div", class_="VwiC3b yXK7lf lVm3ye r025kc hJNv6b Hdw6tb")
        description = description_element.text if description_element else "No description found"

        # Add the title and description to the results list
        results.append({"title": title, "description": description})

# Print the results
for result in results[:5]:
    print(f"Title: {result['title']}")
    print(f"Description: {result['description']}")
    print("----------------------------------")

    keywords.update(result['description'].split())

# Save the results to the respective JSON file
with open('results.json', 'w') as f:
    json.dump(results, f, indent=4)

with open('keywords.json', 'w') as f:
    json.dump(dict(keywords), f, indent=4)