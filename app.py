from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Location Intelligence ADK Agent is running 🌍"

@app.route("/bigquery")
def bigquery():
    return "Fetching data from BigQuery dataset 📊"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)