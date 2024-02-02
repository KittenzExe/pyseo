#soo yeah it's an edit, idk what i say else
import requests
from bs4 import BeautifulSoup
import json
from collections import Counter
from fake_headers import Headers
from urlextract import URLExtract
import time
import ua_generator
import socks
import socket
import random
 
 
extractor = URLExtract()
# Define the search query
 
# Define the number of pages to scrape
num_pages = 10
 
# Create a list to store the results
results = []
"""
# Set the headers for the request
def a():
    with open("User-Agent.txt", "r", encoding="utf8") as f:
        agents = f.read().split("\n")
        for u in agents:
            miykle = {u}
            return miykle
            break
"""
def RandStr():
    with open("text-output.txt", "r") as f:
        words = f.read(random.randint(3, 9)).split("\n")
        for w in words:
            return w
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
 
"""
def headers():
    if __name__ == "__main__":
        header = Headers(
            browser="chrome",  # Generate only Chrome UA
            os="win",  # Generate ony Windows platform
            headers=True  # generate misc headers
        )
        return header.generate()
"""
 
with open("dorks.txt", "r", encoding="utf8") as f:
        dorks = f.read().split("\n")
        for d in dorks:
            with open("http.txt", "r") as f:
                proxies = f.read().split("\n")
                for p in proxies:
                    print(d)
                    print(p)
                    for page_num in range(1, num_pages + 1):
                        requests.get("https://www.google.com/",proxies={"http": p}, timeout=10, headers=headers)
                        url2 = f"https://www.google.com/search?q={RandStr()}&start={0}"
                        response2 = requests.get(url2,proxies={'http': p}, timeout=10, headers=headers)
                        print(RandStr())
                        print(response2.status_code)
                        time.sleep(3)
                        url = f"https://www.google.com/search?q={d}&start={(page_num - 1) * 10}"
                        print(url)
                        response = requests.get(url,proxies={'socks5': p}, timeout=10, headers=headers)
                        time.sleep(3)
                        #print(headers())
                        print(response.status_code)
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, "html.parser")
                            search_results = soup.find_all("div", class_="g")
                            for result in search_results:
                                Site_element = result.find("cite")
                                Site = Site_element.text if Site_element else "No Site found"
                                results.append({"Site": Site})
                                with open('results.txt', 'a') as f:
                                    for result in results:
                                        url = extractor.find_urls(result['Site'])[0]
                                        url = url.replace("https://", "")
                                        url = url.replace("http://", "")  
                                        url = url.replace("www.", "")
                                        f.write(url)
                                        f.write('\n')
                                        print({result['Site']})
                        else:
                            break
