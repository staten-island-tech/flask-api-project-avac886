from flask import Flask, render_template
import requests

app = Flask(__name__)

hpHouses = [
    {"id": 1, "house": "Gryffindor", "description": "Gryffindor students are known for their bravery, courage, and determination, with a strong sense of justice and a love for the underdog. They are often described as daring, passionate, and quick-thinking, willing to take risks and stand up for what they believe in.", "picture": ""},
    {"id": 2, "house": "Hufflepuff", "description": "Hufflepuffs in the Harry Potter universe are known for their strong sense of loyalty, hard work, dedication, fairness, and a belief in teamwork. They value these traits above all else and are often characterized as humble, kind, and patient. Hufflepuffs are also known for their dedication to what they do and their focus on doing things properly.", "picture": ""},
    {"id": 3, "house": "Ravenclaw", "description": "Ravenclaws are known for their intelligence, wisdom, wit, and creativity. They value learning and intellectual pursuits, and often possess a unique perspective and are open-minded.", "picture": ""},
    {"id": 4, "house": "Slytherin", "description": "Slytherin traits include ambition, cunning, leadership, resourcefulness, determination, and a strong sense of self-preservation. They are also known for their intelligence, shrewdness, and a tendency to prioritize their own goals and well-being.", "picture": ""}
]

@app.route("/")
def home():
    return render_template("index.html", hpHouses=hpHouses)

@app.route("/house/<string:name>") #don't like in href the house html, use the thing you put in your app py
def house(name):
    response = requests.get(f"https://hp-api.onrender.com/api/characters/house/{name}")
    members_list = response.json()
    members = []

    for member in members_list:
        members.append({
            'name': member['name'],
            'image': member['image']
        })

    '''print(members)'''
    return render_template("members.html", members=members)

@app.route("/character/<string:id>")
def character(id):
    response = requests.get(f"https://hp-api.onrender.com/api/character/{id}")
    data = response.json()

    name = data.get('name')
    ancestry = data.get('ancestry')
    birth_year = data.get('yearOfBirth')
    wand = data.get('wand', {})
    wand_description = f"{wand.get('wood', 'unknown')} wood, {wand.get('core', 'unknown')} core, {wand.get('lenght', 'unknown')} inches)"
    '''wand = [material['material']['name'] for material in data['wand']]'''
    patronus = data.get('patronus')

    return render_template("character.html", character={
        'name': name,
        'ancestry': ancestry,
        'birth_year': birth_year,
        'wand': wand_description,
        'patronus': patronus
    })

if __name__ == '__main__':
    app.run(debug=True)

""" # get from single house and then idividual character by doing character/id or character/name

@app.route("/house/<string:name>/<id>")
def house_detail(name, id):
    for house in hpHouses:
        response = requests.get(f"https://hp-api.onrender.com/api/characters/house/{name}")
        data = response.json()
        house_list = data['results']
        house_members = []
        for member in house_list:
            response = requests.get(f"https://hp-api.onrender.com/api/character/{id}")
            member = response.json()

            name = member.get('name')
            species = member.get('species')
            dateOfBirth = member.get('dateOfBirth')
            ancestry = member.get('ancestry')
            eyeColor = member.get('eyeColor')
            hairColor = member.get('hairColor')
            wandMaterial = [material['wand'] for material in data['wand']]
            patronus = member.get('patronus')
            image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"

            return render_template("house.html", house ={
            'name': name,
            'id': id,
            'species': species,
            'dateOfBirth': dateOfBirth,
            'ancestry': ancestry,
            'eyeColor': eyeColor,
            'hairColor': hairColor,
            'wandMaterial': wandMaterial,
            'patronus': patronus,
            'image': image_url
        }) 
 """