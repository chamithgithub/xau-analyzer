# sentiment_analyzer.py

from textblob import TextBlob

# Define event-impact keywords
BULLISH_KEYWORDS = [
    "war", "conflict", "crisis", "invasion", "inflation", "recession",
    "unrest", "attack", "geopolitical", "sanction", "tension"
]

BEARISH_KEYWORDS = [
    "rate hike", "interest rate", "hawkish", "strong dollar", "tightening",
    "economic growth", "job growth", "robust economy"
]

def analyze_article_sentiment(article):
    """
    Analyze sentiment of one article and determine impact on XAU/USD
    """
    title = article.get("title", "")
    description = article.get("description", "")
    full_text = f"{title} {description}".lower()

    # Sentiment polarity using TextBlob
    polarity = TextBlob(full_text).sentiment.polarity

    # Rule-based keyword matching
    impact = "neutral"
    reason = "No strong signals detected."

    for word in BULLISH_KEYWORDS:
        if word in full_text:
            impact = "bullish"
            reason = f"Detected keyword: '{word}' – potential gold uptrend."
            break

    for word in BEARISH_KEYWORDS:
        if word in full_text:
            impact = "bearish"
            reason = f"Detected keyword: '{word}' – potential gold downtrend."
            break

    # Combine with sentiment for confidence
    sentiment = "positive" if polarity > 0.1 else "negative" if polarity < -0.1 else "neutral"

    return {
        "impact": impact,
        "sentiment": sentiment,
        "confidence": abs(polarity),
        "reason": reason,
        "title": title,
    }


from core.decision_engine import determine_final_signal

def analyze_articles(news_articles):
    results = [analyze_article_sentiment(article) for article in news_articles]
    decision = determine_final_signal(results)

    return {
        "signal": decision["signal"],
        "articles": results,
        "reason": decision["reason"],
        "breakdown": {
            "bullish": decision["bullish"],
            "bearish": decision["bearish"],
            "neutral": decision["neutral"]
        }
    }


# Test it standalone
if __name__ == "__main__":
    from news_fetcher import fetch_latest_news
    articles = fetch_latest_news()
    analysis = analyze_articles(articles)

    print(f"\n📊 Final XAUUSD Signal: {analysis['signal']}")
    print(f"🔍 Reason: {analysis['reason']}\n")

    for a in analysis['articles']:
        print(f"📰 {a['title']}")
        print(f"   Impact: {a['impact']}, Sentiment: {a['sentiment']}, Confidence: {a['confidence']:.2f}")
        print(f"   ➤ {a['reason']}")
        print()
