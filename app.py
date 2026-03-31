from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "My ADK Agent is running 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # 👈 IMPORTANT
    app.run(host="0.0.0.0", port=port)