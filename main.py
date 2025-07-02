# main.py
# A.C.Dilshan

from api.news_fetcher import fetch_latest_news
from api.sentiment_analyzer import analyze_articles
from core.utils import save_log_entry, get_timestamp, print_signal_summary

if __name__ == "__main__":
    news = fetch_latest_news()
    result = analyze_articles(news)
    
    print_signal_summary(result)

    save_log_entry({
        "timestamp": get_timestamp(),
        "signal": result["signal"],
        "reason": result["reason"],
        "articles": result["articles"]
    })
