from flask import Flask, render_template
import requests

app = Flask(__name__)

hpHouses = [
    {"id": 1, "house": "Gryffindor", "description": "Gryffindor students are known for their bravery, courage, and determination, with a strong sense of justice and a love for the underdog. They are often described as daring, passionate, and quick-thinking, willing to take risks and stand up for what they believe in."},
    {"id": 2, "house": "Hufflepuff", "description": "Hufflepuffs in the Harry Potter universe are known for their strong sense of loyalty, hard work, dedication, fairness, and a belief in teamwork. They value these traits above all else and are often characterized as humble, kind, and patient. Hufflepuffs are also known for their dedication to what they do and their focus on doing things properly."},
    {"id": 3, "house": "Ravenclaw", "description": "Ravenclaws are known for their intelligence, wisdom, wit, and creativity. They value learning and intellectual pursuits, and often possess a unique perspective and are open-minded."},
    {"id": 4, "house": "Slytherin", "description": "Slytherin traits include ambition, cunning, leadership, resourcefulness, determination, and a strong sense of self-preservation. They are also known for their intelligence, shrewdness, and a tendency to prioritize their own goals and well-being. "}
]

@app.route("/")
def home():
    return render_template("index.html", hpHouses=hpHouses)

""" @app.route("/house:house") """



""" @app.route("/gryffindor")
def gryffindor():
    response = requests.get("https://hp-api.onrender.com/api/characters/house/gryffindor")
    data = response.json()
    gryffindor_list = data['results']
    gryffindors = []

    for gryffindor in gryffindor_list:
        image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"
        gryffindors.append({
            'name': gryffindor['name'],
            'id': id,
            'image': image_url
        })
    return render_template("gryffindors.html", gryffindors=gryffindors) """

""" @app.route("/gryffindor/<int:id>")
def gryffindor_detail(id):
    response = requests.get("https://hp-api.onrender.com/api/characters/house/gryffindor{id}")
    data = response.json()

    name = data.get('name')
    species = data.get('species')
    dateOfBirth = data.get('dateOfBirth')
    ancestry = data.get('ancestry')
    eyeColor = data.get('eyeColor')
    hairColor = data.get('hairColor')
    wandMaterial = [material['wand'] for material in data['wand']]
    patronus = data.get('patronus')
    image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"

    return render_template("gryffindor.html", gryffindor ={
        'name': name,
        'id': id,
        'species': species,
        'dateOfBirth': dateOfBirth,
        'ancestry': ancestry,
        'eyeColor': eyeColor,
        'hairColor': hairColor,
        'wandMaterial': wandMaterial,
        'patronus': patronus
    }) """

""" @app.route("/hufflepuff")
def hufflepuff():
    response = requests.get("https://hp-api.onrender.com/api/characters/house/hufflepuff")
    data = response.json()
    hufflepuff_list = data['results']
    hufflepuffs = []

    for hufflepuff in hufflepuff_list:
        image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"
        hufflepuffs.append({
            'name': hufflepuff['name'],
            'id': id,
            'image': image_url
        })
    return render_template("hufflepuffs.html", hufflepuffs=hufflepuffs) """
    
""" @app.route("/hufflepuff/<int:id>")
def hufflepuff_detail(id):
    response = requests.get("https://hp-api.onrender.com/api/characters/house/hufflepuff{id}")
    data = response.json()
    
    name = data.get('name')
    species = data.get('species')
    dateOfBirth = data.get('dateOfBirth')
    ancestry = data.get('ancestry')
    eyeColor = data.get('eyeColor')
    hairColor = data.get('hairColor')
    wandMaterial = [material['wand'] for material in data['wand']]
    patronus = data.get('patronus')
    image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"

    return render_template("hufflepuff.html", hufflepuff ={
        'name': name,
        'id': id,
        'species': species,
        'dateOfBirth': dateOfBirth,
        'ancestry': ancestry,
        'eyeColor': eyeColor,
        'hairColor': hairColor,
        'wandMaterial': wandMaterial,
        'patronus': patronus
    }) """

""" @app.route("/ravenclaw")
def ravenclaw():
    response = response.get("https://hp-api.onrender.com/api/characters/house/:house")
    data = response.json
    ravenclaw_list = data['results']
    ravenclaws = []

    for ravenclaw in ravenclaw_list:
        image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"
        ravenclaws.append({
            'name': ravenclaw['name'],
            'id': id,
            'image': image_url
        })
    return render_template("ravenclaws.html", ravenclaws=ravenclaws) """

""" @app.route("/ravenclaw/<int:id>")
def ravenclaw_detail(id):
    response = response.get(f"https://hp-api.onrender.com/api/characters/house/ravenclaw{id}")
    data = response.json()

    name = data.get('name')
    species = data.get('species')
    dateOfBirth = data.get('dateOfBirth')
    ancestry = data.get('ancestry')
    eyeColor = data.get('eyeColor')
    hairColor = data.get('hairColor')
    wandMaterial = [material['wand'] for material in data['wand']]
    patronus = data.get('patronus')
    image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"

    return render_template("ravenclaw.html", ravenclaw ={
        'name': name,
        'id': id,
        'species': species,
        'dateOfBirth': dateOfBirth,
        'ancestry': ancestry,
        'eyeColor': eyeColor,
        'hairColor': hairColor,
        'wandMaterial': wandMaterial,
        'patronus': patronus
    }) """

""" @app.route("/slytherin")
def slytherin():
    response = response.get("https://hp-api.onrender.com/api/characters/house/slytherin")
    data = response.json()
    slytherin_list = data['results']
    slytherins = []

    for slytherin in slytherin_list:
        image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"
        slytherins.append({
            'name': slytherin['name'],
            'id': id,
            'image': image_url
        })
    return render_template("slytherins.html", slytherins=slytherins) """

""" @app.route("/slytherin/<int:id>")
def slytherin_detail(id):
    response = requests.get("https://hp-api.onrender.com/api/characters/house/slytherin{id}")
    data = response.json()

    name = data.get('name')
    species = data.get('species')
    dateOfBirth = data.get('dateOfBirth')
    ancestry = data.get('ancestry')
    eyeColor = data.get('eyeColor')
    hairColor = data.get('hairColor')
    wandMaterial = [material['wand'] for material in data['wand']]
    patronus = data.get('patronus')
    image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"

    return render_template("slytherin.html", slytherin ={
        'name': name,
        'id': id,
        'species': species,
        'dateOfBirth': dateOfBirth,
        'ancestry': ancestry,
        'eyeColor': eyeColor,
        'hairColor': hairColor,
        'wandMaterial': wandMaterial,
        'patronus': patronus
    }) """

""" if __name__ == '__main__':
    app.run(debug=True) """
