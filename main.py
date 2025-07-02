# main.py

from api.news_fetcher import fetch_latest_news
from api.sentiment_analyzer import analyze_articles
from core.utils import save_log_entry, get_timestamp, print_signal_summary

def choose_news_source():
    print("\nChoose a news source:")
    print("1. NewsAPI")
    print("2. GNews")
    print("3. FXStreet")
    print("q. Quit")
    choice = input("Enter 1/2/3 or q: ").strip().lower()

    if choice == "1":
        return "newsapi"
    elif choice == "2":
        return "gnews"
    elif choice == "3":
        return "fxstreet"
    elif choice == "q":
        return "quit"
    else:
        print("❌ Invalid choice. Try again.")
        return None

def analyze_source(source):
    print(f"[INFO] Using source: {source.upper()}")

    try:
        news_articles = fetch_latest_news(source=source)
        result = analyze_articles(news_articles)

        print_signal_summary(result)

        save_log_entry({
            "timestamp": get_timestamp(),
            "signal": result["signal"],
            "reason": result["reason"],
            "articles": result["articles"]
        })
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    while True:
        selected_source = choose_news_source()
        if selected_source == "quit":
            print("👋 Exiting XAU/USD analyzer.")
            break
        elif selected_source:
            analyze_source(selected_source)
