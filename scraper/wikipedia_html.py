import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    paragraphs = soup.find_all("p")
    return [p.text for p in paragraphs if p.text.strip()]

