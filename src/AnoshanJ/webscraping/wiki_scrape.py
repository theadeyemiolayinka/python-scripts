import requests
from bs4 import BeautifulSoup

def wikipedia_summary(topic):
    url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Fetching the first few paragraphs under the main heading
    paragraphs = soup.select("div.mw-parser-output > p")
    
    for paragraph in paragraphs:
        # Assuming that a summary would be more than a certain length.
        if len(paragraph.text) > 50:
            return paragraph.text

topic = input("Enter a Wikipedia topic: ")
print(wikipedia_summary(topic))
