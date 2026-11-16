from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_video_python"]

#On établie les perso et leurs stats
characters = [
    ("Guerrier", 15, 10, 100),
    ("Mage", 20, 5, 80),
    ("Archer", 18, 7, 90),
    ("Voleur", 22, 8, 85),
    ("Paladin", 14, 12, 110),
    ("Sorcier", 25, 3, 70),
    ("Chevalier", 17, 15, 120),
    ("Moine", 19, 9, 95),
    ("Berserker", 23, 6, 105),
    ("Chasseur", 16, 11, 100)
]

#On établie les monstres et leurs stats 
monsters = [
    ("Gobelin", 5, 5, 50),
    ("Orc", 10, 8, 120),
    ("Dragon", 18, 20, 300),
    ("Zombie", 6, 6, 70),
    ("Troll", 13, 15, 200),
    ("Spectre", 9, 10, 100),
    ("Golem", 15, 25, 250),
    ("Vampire", 11, 12, 150),
    ("Loup-garou", 14, 18, 180),
    ("Squelette", 8, 7, 90)
]

def init_jeu():
    #On supprime les collections pour éviter les doublons
    db.characters.delete_many({})
    db.monsters.delete_many({})
    #On insère les personnages et les monstres dans la base de données
    db.characters.insert_many([{"name": n, "attack": a, "defense": d, "hp": h} for n, a, d, h in characters])
    db.monsters.insert_many([{"name": n, "attack": a, "defense": d, "hp": h} for n, a, d, h in monsters])