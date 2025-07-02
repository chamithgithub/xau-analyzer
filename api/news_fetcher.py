# news_fetcher.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Load API keys from .env
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

# Choose source: "newsapi" or "gnews"
NEWS_SOURCE = os.getenv("NEWS_SOURCE", "newsapi").lower()

# Common keywords to look for
QUERY = "gold OR XAUUSD OR central bank OR war OR inflation OR fed OR conflict"

def fetch_from_newsapi():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": QUERY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": NEWSAPI_KEY,
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    articles = data.get("articles", [])
    return [
        {
            "title": a["title"],
            "description": a.get("description"),
            "source": a["source"]["name"],
            "publishedAt": a["publishedAt"],
            "url": a["url"]
        }
        for a in articles
    ]


def fetch_from_gnews():
    url = "https://gnews.io/api/v4/search"
    params = {
        "q": QUERY,
        "lang": "en",
        "max": 10,
        "token": GNEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    articles = data.get("articles", [])
    return [
        {
            "title": a["title"],
            "description": a.get("description"),
            "source": a["source"]["name"],
            "publishedAt": a["publishedAt"],
            "url": a["url"]
        }
        for a in articles
    ]


def fetch_latest_news():
    if NEWS_SOURCE == "newsapi":
        print("[INFO] Using NewsAPI")
        return fetch_from_newsapi()
    elif NEWS_SOURCE == "gnews":
        print("[INFO] Using GNews API")
        return fetch_from_gnews()
    else:
        raise ValueError("Unsupported NEWS_SOURCE. Use 'newsapi' or 'gnews'.")


# Test the module
if __name__ == "__main__":
    news = fetch_latest_news()
    for article in news:
        print(f"📰 {article['title']} ({article['source']})")
        print(f"    {article['publishedAt']}")
        print()
