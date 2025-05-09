from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://hp-api.onrender.com/api/characters")
    data = response.json()
    harry_potter_list = data['results']
    characters = []

    for character in harry_potter_list:
        url = character['url']
        parts = url.strip("/").split("/")
        id = parts[-1]

        image_url = f""