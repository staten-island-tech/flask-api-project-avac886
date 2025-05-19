from flask import Flask, render_template
import requests

hpHouses = [
    {"id": 1, "house": "Gryffindor", "description": "Gryffindor students are known for their bravery, courage, and determination, with a strong sense of justice and a love for the underdog. They are often described as daring, passionate, and quick-thinking, willing to take risks and stand up for what they believe in."},
    {"id": 2, "house": "Hufflepuff", "description": "Hufflepuffs in the Harry Potter universe are known for their strong sense of loyalty, hard work, dedication, fairness, and a belief in teamwork. They value these traits above all else and are often characterized as humble, kind, and patient. Hufflepuffs are also known for their dedication to what they do and their focus on doing things properly."},
    {"id": 3, "house": "Ravenclaw", "description": "Ravenclaws are known for their intelligence, wisdom, wit, and creativity. They value learning and intellectual pursuits, and often possess a unique perspective and are open-minded."},
    {"id": 4, "house": "Slytherin", "description": "Slytherin traits include ambition, cunning, leadership, resourcefulness, determination, and a strong sense of self-preservation. They are also known for their intelligence, shrewdness, and a tendency to prioritize their own goals and well-being. "}
] 

for house in hpHouses:
    response = requests.get(f"https://hp-api.onrender.com/api/characters/house/{house['house']}")
    data = response.json()
    house_list = data['results']
    house_members = []
    print(data)

    for member in house_list:
        image_url = f"https://ik.imagekit.io/hpapi/{id}.jpg"
        house_members.append({
            'name': member['name'],
            'id': id,
            'image': image_url
        })
