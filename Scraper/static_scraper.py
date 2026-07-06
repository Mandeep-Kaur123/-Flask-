import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "https://quotes.toscrape.com"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for quote in soup.select(".quote"):
        quotes.append({
            "text": quote.select_one(".text").text,
            "author": quote.select_one(".author").text
        })

    return quotes