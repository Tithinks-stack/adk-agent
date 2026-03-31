from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Location Intelligence ADK Agent is running 🌍"

@app.route("/location")
def location():
    return "Showing location data for Mumbai 📍"

@app.route("/map")
def map_view():
    return "Google Maps integration simulated 🗺️"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)