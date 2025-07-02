from flask import Flask, jsonify, render_template_string
import json
import os

app = Flask(__name__)

# 🔥 Path fix
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, "data", "news_log.json")

# 🔷 HTML styles
STYLE = """
<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    background: #f4f4f9;
    padding: 2rem;
    color: #333;
    max-width: 800px;
    margin: auto;
  }
  h1, h2, h3 {
    color: #111;
  }
  .signal {
    font-size: 1.5rem;
    padding: 1rem;
    background: #e3f2fd;
    border-left: 5px solid #2196f3;
    margin-bottom: 1.5rem;
  }
  .articles {
    list-style: none;
    padding: 0;
  }
  .articles li {
    margin-bottom: 1rem;
    padding: 1rem;
    background: #fff;
    border-left: 4px solid #ccc;
    box-shadow: 0 0 5px rgba(0,0,0,0.05);
  }
  .articles li.bullish { border-color: #4caf50; }
  .articles li.bearish { border-color: #f44336; }
  .articles li.neutral { border-color: #9e9e9e; }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 2rem;
  }
  th, td {
    border: 1px solid #ccc;
    padding: 0.6rem;
    text-align: left;
  }
  th {
    background: #e0e0e0;
  }
</style>
"""

@app.route("/")
def home():
    if not os.path.exists(LOG_PATH):
        return "No data available."

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        return "No data available."

    latest = data[-1]

    return render_template_string(STYLE + """
    <h1>📊 Latest XAU/USD Signal</h1>

    <div class="signal">
      <strong>Signal:</strong> {{ latest.signal }} <br>
      <strong>Reason:</strong> {{ latest.reason }} <br>
      <strong>Time:</strong> {{ latest.timestamp }}
    </div>

    <h3>📰 Top News Articles</h3>
    <ul class="articles">
      {% for a in latest.articles[:3] %}
        <li class="{{ a.impact|lower }}">
          <strong>{{ a.title }}</strong><br>
          Sentiment: {{ a.sentiment }} | Impact: {{ a.impact }}
        </li>
      {% endfor %}
    </ul>
    <a href="/history">🔁 View Signal History</a>
    """, latest=latest)

@app.route("/api")
def api():
    if not os.path.exists(LOG_PATH):
        return jsonify({"error": "No data"}), 404

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    return jsonify(data[-1])

@app.route("/history")
def history():
    if not os.path.exists(LOG_PATH):
        return "No data available."

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    return render_template_string(STYLE + """
        <h2>📚 XAU/USD Signal History</h2>
        <table>
          <tr><th>Timestamp</th><th>Signal</th><th>Reason</th></tr>
          {% for entry in data|reverse %}
            <tr>
              <td>{{ entry.timestamp }}</td>
              <td>{{ entry.signal }}</td>
              <td>{{ entry.reason }}</td>
            </tr>
          {% endfor %}
        </table>
        <br><a href="/">⬅ Back to Latest Signal</a>
    """, data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
