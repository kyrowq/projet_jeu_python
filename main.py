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
            return choix
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
    enregistrer_le_score(pseudo, numero_manche)

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

#Combattre la manche()
#   Mettre dans monstres le résultat de Créer les monstres de la manche()
#   Tant que Il reste des vivants() du coté de l'équipe et Il reste des vivants() du coté des monstres
#       Jouer le tour d'un camp() l'équipe attaque les monstres
#       Si Il reste des vivants () du coté des monstres
#           Jouer le tour d'un camp() les monstres attaquent l'équipe
#   Si il reste des vivants() du coté de l'équipe
#       Afficher que la manche est réussie
#   Retourner si Il reste des vivants() ou non dans l'équipe

#Créer les monstres de la manche()
#   Mettre dans monstres disponibles le résultat de Lire les monstres()
#   Tirer 3 monstres au hasard() parmi ceux qui sont disponibles

#Lire les monstres()
#   Lire la collection monstres dans la base de données
#   Retourner la liste des monstres

#Tirer 3 monstres au hasard()
#   Choisir 3 monstres differents au hasard dans la liste
#   Retourner ces 3 monstres

#Jouer le tour d'un camp()
#   Pour chaque attaquant vivant
#       Si Il ne reste plus de vivants() défenseurs
#           Sortir de la boucle
#       Mettre dans cible le résultat de Choisir une cible()
#       Mettre dans dégats le résultat de Attaquer()
#       Afficher le résultat de l'attaque()

#Lister les vivants()
#   Créer une liste vide
#   Pour chaque membre du camp
#       Si le membre est vivant
#           Ajouter le membre à la liste
#   Retourner la liste

#Il reste des vivants()
#   Retourner VRAI si la liste des vivants() n'est pas vide, sinon FAUX

#Choisir une cible()
#   Retourner un  membre au hasard dans la liste des vivants() du camp adverse

#Attaquer()
#   Mettre dans dégats le résultat de Calculer les dégats() de l'attaquant à la cible
#   Appliquer les dégats() à la cible
#   Retourner les dégats

#Calculer les dégats()
#	Mettre dans dégats l'attaque de l'attaquant moins la défense de la cible
#	Si les dégats sont inférieurs à 1
#		Mettre les dégats à 1
#	Retourner les dégats

#Appliquer les dégats()
#   Retirer les dégats aux points de vie de la cible
#   Si les points de vie de la cible sont égaux à 0 ou moins
#       Mettre les points de vie à 0
#       Marquer la cible comme morte

#Afficher le résultat de l'attaque()
#   Afficher que l'attaquant attaque la cible et lui inflige les dégats
#   Si la cible est morte
#       Afficher que la cible est morte

#Enregistrer les scores()
#   Mettre dans pseudo du joueur le résultat de Demander au joueur son pseudo()
#   Créer un score avec le pseudo du joueur et la manche atteinte
#   Ajouter le score à la collection scores de la base de données

#Afficher les scores()

lancer_le_programme()