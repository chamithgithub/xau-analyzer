from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
from api.news_fetcher import fetch_latest_news
from api.sentiment_analyzer import analyze_articles

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Main handler for /xauusd
async def xauusd_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔎 Analyzing latest global news for XAU/USD prediction...")

    news_articles = fetch_latest_news()
    result = analyze_articles(news_articles)

    signal = result["signal"]
    reason = result["reason"]
    articles = result["articles"]

    # Build response message
    emoji = {"UP": "📈", "DOWN": "📉", "NORMAL": "🟡"}
    message = f"""{emoji.get(signal)} XAU/USD Signal: *{signal}*
🧠 Reason: _{reason}_

📰 *Top Headlines Impacting Gold*:
"""

    for article in articles[:3]:  # show top 3 articles
        message += f"\n- *{article['title']}*\n  Impact: `{article['impact']}` | Sentiment: `{article['sentiment']}`"

    await update.message.reply_markdown(message)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to the XAU/USD Gold Signal Bot.\nUse /xauusd to get the latest news-based gold trend prediction.")

# Set up bot
def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("xauusd", xauusd_signal))

    print("✅ Telegram bot running. Type /xauusd in chat.")
    app.run_polling()

# Run standalone
if __name__ == "__main__":
    run_bot()
