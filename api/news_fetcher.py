# api/news_fetcher.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

from api.fxstreet_fetcher import fetch_fxstreet_news

# API keys
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

QUERY = "gold OR XAUUSD OR central bank OR war OR inflation OR fed OR conflict"

def fetch_from_newsapi(limit=10):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": QUERY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": limit,
        "apiKey": NEWSAPI_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return [
        {
            "title": a["title"],
            "description": a.get("description"),
            "source": a["source"]["name"],
            "publishedAt": a["publishedAt"],
            "url": a["url"]
        } for a in data.get("articles", [])
    ]

def fetch_from_gnews(limit=10):
    url = "https://gnews.io/api/v4/search"
    params = {
        "q": QUERY,
        "lang": "en",
        "max": limit,
        "token": GNEWS_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return [
        {
            "title": a["title"],
            "description": a.get("description"),
            "source": a["source"]["name"],
            "publishedAt": a["publishedAt"],
            "url": a["url"]
        } for a in data.get("articles", [])
    ]

def fetch_latest_news(source="newsapi"):
    print(f"[INFO] Using source: {source.upper()}")
    if source == "newsapi":
        return fetch_from_newsapi()
    elif source == "gnews":
        return fetch_from_gnews()
    elif source == "fxstreet":
        return fetch_fxstreet_news()
    else:
        raise ValueError("Unsupported source. Use 'newsapi', 'gnews', or 'fxstreet'.")
