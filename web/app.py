# web/app.py

from flask import Flask, jsonify, render_template_string
import json
import os

app = Flask(__name__)
LOG_PATH = os.path.join("..", "data", "news_log.json")

@app.route("/")
def home():
    if not os.path.exists(LOG_PATH):
        return "No data available."

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    latest = data[-1] if data else {}

    return render_template_string("""
        <h2>📊 Latest XAU/USD Signal</h2>
        <p><strong>Signal:</strong> {{ latest.signal }}</p>
        <p><strong>Reason:</strong> {{ latest.reason }}</p>
        <p><strong>Timestamp:</strong> {{ latest.timestamp }}</p>

        <h3>📰 Top News</h3>
        <ul>
        {% for a in latest.articles[:3] %}
          <li><strong>{{ a.title }}</strong> – {{ a.impact }} ({{ a.sentiment }})</li>
        {% endfor %}
        </ul>
    """, latest=latest)

@app.route("/api")
def api():
    if not os.path.exists(LOG_PATH):
        return jsonify({"error": "No data"}), 404

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    return jsonify(data[-1])  # Latest entry

if __name__ == "__main__":
    app.run(debug=True, port=5000)
