# api/fxstreet_fetcher.py

import feedparser
from datetime import datetime

def fetch_fxstreet_news():
    rss_url = "https://www.fxstreet.com/rss/news"  # General news feed
    feed = feedparser.parse(rss_url)

    articles = []
    for entry in feed.entries[:10]:  # Get latest 10 entries
        articles.append({
            "title": entry.title,
            "description": entry.get("summary", ""),
            "source": "FXStreet",
            "publishedAt": entry.published if "published" in entry else "",
            "url": entry.link
        })

    return articles
