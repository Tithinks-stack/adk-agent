from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Location Intelligence ADK Agent is running 🌍"

@app.route("/alloydb")
def alloydb():
    return "AlloyDB database setup successful 🗄️"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)