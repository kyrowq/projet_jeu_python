from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_video_python"]

#On établie les perso et leurs stats
characters = [
    ("Guerrier", 16, 6, 280),
    ("Mage", 22, 2, 190),
    ("Archer", 19, 3, 220),
    ("Voleur", 20, 4, 210),
    ("Paladin", 14, 9, 320),
    ("Sorcier", 24, 1, 180),
    ("Chevalier", 15, 10, 330),
    ("Moine", 17, 5, 250),
    ("Berserker", 21, 3, 240),
    ("Chasseur", 18, 5, 230)
]

#On établie les monstres et leurs stats
monsters = [
    ("Gobelin", 5, 2, 40),
    ("Orc", 9, 4, 90),
    ("Dragon", 16, 8, 220),
    ("Zombie", 7, 2, 70),
    ("Troll", 12, 6, 150),
    ("Spectre", 10, 5, 80),
    ("Golem", 13, 10, 180),
    ("Vampire", 11, 5, 100),
    ("Loup-garou", 12, 4, 110),
    ("Squelette", 8, 3, 60)
]

def init_jeu():
    #On supprime les collections pour éviter les doublons
    db.characters.delete_many({})
    db.monsters.delete_many({})
    #On insère les personnages et les monstres dans la base de données
    db.characters.insert_many([{"name": n, "attack": a, "defense": d, "hp": h} for n, a, d, h in characters])
    db.monsters.insert_many([{"name": n, "attack": a, "defense": d, "hp": h} for n, a, d, h in monsters])