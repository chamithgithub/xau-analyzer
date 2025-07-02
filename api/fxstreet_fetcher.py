# api/fxstreet_fetcher.py
import feedparser

FXSTREET_RSS = "https://www.fxstreet.com/rss/commodities"

def fetch_fxstreet_news(limit=5):
    feed = feedparser.parse(FXSTREET_RSS)
    entries = feed.entries[:limit]
    return [
        {
            "title": e.title,
            "published": e.published,
            "summary": e.summary,
            "url": e.link,
            "source": "FXStreet"
        }
        for e in entries
    ]
