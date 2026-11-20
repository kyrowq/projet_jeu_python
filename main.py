import random

from db_init import db, init_jeu

TAILLE_EQUIPE = 3

def decrire_une_option(option):
#   Si l'option est un personnage
    if isinstance(option, dict):
#       Retoruner le nom du personnage, son attaque, sa défense et ses points de vie
        return (f"{option['name']} - Attaque : {option['attack']} - Défense : {option['defense']} - PV : {option['hp']}")
#   Retourner l'option
    return option

def afficher_les_options(options):
#   Pour chaque option de la liste
    for numero, option in enumerate(options, start=1):
#       Afficher son numéro et sa description
        print(f"{numero}. {decrire_une_option(option)}")

def verifier_si_le_choix_est_valide(choix, minimum, maximum):
#   Si ce n'est pas un digit
    if not choix.isdigit():
#       Retourne FAUX
        return False
#   Convertir le choix du joueur en entier
    choix = int(choix)
#   Si le choix du joueur est inférieur au minimum ou supérieur au maximum
    if choix < minimum or choix > maximum:
#       Retourne FAUX
        return False
#   Retourne VRAI
    return True

def obtenir_un_choix_valide(options):
#   Tant que infini
    while True:
#       Afficher les options()
        afficher_les_options(options)
#       Demander au joueur son choix
        choix = input("Ton choix : ")
#       Si le choix est valide()
        if verifier_si_le_choix_est_valide(choix, 1, len(options)):
#           Retourner le choix du joueur
            return int(choix)
#       Afficher une erreur
        print("\nChoix invalide, entre un des numéros proposés.")

def lancer_le_programme():
#   Créer la liste des options du menu
    options_du_menu = ["Lancer le jeu", "Tableau des scores", "Quitter le jeu"]
#   Tant que infini
    while True:
#       Mettre dans la variable choix le résultat de Obtenir un choix valide()
        choix = obtenir_un_choix_valide(options_du_menu)
#       Executer le choix()
        executer_le_choix(choix)

def executer_le_choix(choix):
#   Selon le choix
    if choix == 1:
#       choix 1: Lancer le jeu()
        lancer_le_jeu()
    if choix == 2:
#       choix 2: Afficher les scores()
        afficher_les_scores()
    if choix == 3:
#       choix 3: Quitter le jeu()
        quitter_le_jeu()

def lancer_le_jeu():
#   Demander au joueur son pseudo()
    pseudo = demander_au_joueur_son_pseudo()
#   Composer l'équipe()
    equipe = composer_equipe()
#   Initialiser le numéro de la manche à 1
    numero_manche = 1
#   Tant que Combattre la manche()
    while combattre_la_manche(equipe):
#       Ajouter 1 au numéro de la manche
        numero_manche += 1
#   Afficher la fin de partie avec le nombre de manche atteinte
    print(f"Fin de partie ! Ton équipe a atteint la manche {numero_manche}.")
#   Enregistrer les scores()
    enregistrer_les_scores(pseudo, numero_manche)

def demander_au_joueur_son_pseudo():
#   Tant que infini
    while True:
#       Demander le pseudo du joueur
        pseudo = input("Entrer votre pseduo : ").strip()
#       Si le pseudo n'est pas vide
        if pseudo != "":
#           Retourner le pseudo
            return pseudo
#       Afficher une erreur
        print("Le pseudo ne peut pas être vide.")

def composer_equipe():
#   Mettre dans persos disponibles le résultat de Lire les persos()
    persos_disponibles = lire_les_persos()
#   Créer une équipe vide
    equipe = []
#   Tant que l'équipe n'est pas complète
    while len(equipe) < TAILLE_EQUIPE:
#       Mettre dans choix le résultat de Obtenir un choix valide()
        choix = obtenir_un_choix_valide(persos_disponibles)
#       Mettre dans perso choisi le numéro du personnage disponible choisi par le joueur
        perso_choisi = persos_disponibles[choix - 1]
#       Ajouter une copie du perso choisi à l'équipe
        equipe.append(dict(perso_choisi, vivant = True))
#       Retirer le perso choisi des personnages disponnibles
        persos_disponibles.remove(perso_choisi)
#   Retourner l'équipe
    return equipe

def lire_les_persos():
#   Lire la collection characters dans la base de données et retourner la liste des persos
    return list(db.characters.find({}, {"_id": 0}))

def combattre_la_manche(equipe):
#   Mettre dans monstres le résultat de Créer les monstres de la manche()
    monstres = creer_les_monstres_de_la_manche()
#   Tant que Il reste des vivants() du coté de l'équipe et Il reste des vivants() du coté des monstres
    while il_reste_des_vivants(equipe) and il_reste_des_vivants(monstres):
#       Jouer le tour d'un camp() l'équipe attaque les monstres
        jouer_le_tour_d_un_camp(equipe, monstres)
#       Si Il reste des vivants () du coté des monstres
        if il_reste_des_vivants(monstres):
#           Jouer le tour d'un camp() les monstres attaquent l'équipe
            jouer_le_tour_d_un_camp(monstres, equipe)
#   Si il reste des vivants() du coté de l'équipe
    if il_reste_des_vivants(monstres):
#       Afficher que la manche est réussie
        print("\nLa manche est réussie !")
#   Retourner si Il reste des vivants() ou non dans l'équipe
    return il_reste_des_vivants(equipe)

def creer_les_monstres_de_la_manche():
#   Mettre dans monstres disponibles le résultat de Lire les monstres()
    monstres_disponibles = lire_les_monstres()
#   Tirer 3 monstres au hasard() parmi ceux qui sont disponibles
    monstres_tires = tirer_3_monstres_au_hasard(monstres_disponibles)
#   On ajoute l'état "vivant" à chaque monstre
    return [dict(monstre, vivant = True) for monstre in monstres_tires]

def lire_les_monstres():
#   Lire la collection monstres dans la base de données et retourner la liste des monstres
    return list(db.monsters.find({}, {"_id": 0}))

def tirer_3_monstres_au_hasard(monstres):
#   Choisir 3 monstres differents au hasard dans la liste et les retourner
    return random.sample(monstres, 3)

def jouer_le_tour_d_un_camp(attaquants, defenseurs):
#   Pour chaque attaquant vivant
    for attaquant in lister_les_vivants(attaquants):
#       Si Il ne reste plus de vivants() défenseurs
        if not il_reste_des_vivants(defenseurs):
#           Sortir de la boucle
            break
#       Mettre dans cible le résultat de Choisir une cible()
        cible = choisir_une_cible(defenseurs)
#       Mettre dans dégats le résultat de Attaquer()
        degats = attaquer(attaquant, cible)
#       Afficher le résultat de l'attaque()
        afficher_le_resultat_de_l_attaque(attaquant, cible, degats)

def lister_les_vivants(camp):
#   Créer une liste vide
    vivants = []
#   Pour chaque membre du camp
    for membre in camp:
#       Si le membre est vivant
        if membre["vivant"]:
#           Ajouter le membre à la liste
            vivants.append(membre)
#   Retourner la liste
    return vivants

def il_reste_des_vivants(camp):
#   Retourner VRAI si la liste des vivants() n'est pas vide, sinon FAUX
    return len(lister_les_vivants(camp)) > 0

def choisir_une_cible(camp_adverse):
#   Retourner un  membre au hasard dans la liste des vivants() du camp adverse
    return random.choice(lister_les_vivants(camp_adverse))

def attaquer(attaquant, cible):
#   Mettre dans dégats le résultat de Calculer les dégats() de l'attaquant à la cible
    degats = calculer_les_degats(attaquant, cible)
#   Appliquer les dégats() à la cible
    appliquer_les_degats(cible, degats)
#   Retourner les dégats
    return degats

def calculer_les_degats(attaquant, cible):
#	Mettre dans dégats l'attaque de l'attaquant moins la défense de la cible
    degats = attaquant["attack"] - cible["defense"]
#	Si les dégats sont inférieurs à 1
    if degats < 1:
#		Mettre les dégats à 1
        degats = 1
#	Retourner les dégats
    return degats

def appliquer_les_degats(cible, degats):
#   Retirer les dégats aux points de vie de la cible
    cible["hp"] -= degats
#   Si les points de vie de la cible sont égaux à 0 ou moins
    if cible["hp"] <= 0:
#       Mettre les points de vie à 0
        cible["hp"] = 0
#       Marquer la cible comme morte
        cible["vivant"] = False

def afficher_le_resultat_de_l_attaque(attaquant, cible, degats):
#   Afficher que l'attaquant attaque la cible et lui inflige les dégats
    print(f"{attaquant['name']} attaque {cible['name']} et lui inflige"
          f"{degats} dégats (PV restants : {cible['hp']})")
#   Si la cible est morte
    if not cible["vivant"]:
#       Afficher que la cible est morte
        print(f"  -> {cible['name']} est mort !")

#Enregistrer les scores()
#   Mettre dans pseudo du joueur le résultat de Demander au joueur son pseudo()
#   Créer un score avec le pseudo du joueur et la manche atteinte
#   Ajouter le score à la collection scores de la base de données

#Afficher les scores()
#   Mettre dans meilleurs scores le résultat de Lire les meilleurs scores()
#   Si la liste des meilleurs scores est vide
#       Afficher qu'il n'y a pas encore de score
#   Sinon
#       Afficher la liste des scores

#Lire les meilleurs scores()
#   Mettre dans scores le trie de la manche la plus élevée à la moins élevée
#   Retourner la liste des scores

#Afficher la liste des scores()
#   Pour chaque score de la liste
#       Afficher son rang, le nom du joueur et la manche atteinte

lancer_le_programme()