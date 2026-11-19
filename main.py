#Afficher les options()
#   Pour chaque option de la liste
#       Afficher son numéro et sa description

#Vérifier si le choix est valide()
#   Si ce n'est pas un digit
#       Retourne FAUX
#   Convertir le choix du joueur en entier
#   Si le choix du joueur est inférieur au minimum ou supérieur au maximum
#       Retourne FAUX
#   Retourne VRAI

#Obtenir un choix valide()
#   Tant que infini
#       Afficher les options()
#       Demander au joueur son choix
#       Si le choix est valide()
#           Retourner le choix du joueur
#       Afficher une erreur

#Lancer le programme()
#   Créer la liste des options du menu
#   Tant que infini
#       Mettre dans la variable choix le résultat de Obtenir un choix valide()
#       Executer le choix()

#Executer le choix()
#   Selon le choix
#       choix 1: Lancer le jeu()
#       choix 2: Afficher les scores()
#       choix 3: Quitter le jeu()

#Lancer le jeu()
#   Demander au joueur son pseudo()
#   Composer l'équipe()
#   Initialiser le numéro de la manche à 1
#   Tant que Combattre la manche()
#       Ajouter 1 au numéro de la manche
#   Afficher la fin de partie avec le nombre de manche atteinte
#   Enregistrer les scores()

#Affiher les scores()

#Demander au joueur son pseudo()
#   Tant que infini
#       Demander le pseudo du joueur
#       Si le pseudo n'est pas vide
#           Retourner le pseudo
#       Afficher une erreur

#Composer l'équipe()
#   Mettre dans persos disponibles le résultat de Lire les persos()
#   Créer une équipe vide
#   Tant que l'équipe n'est pas complète
#       Mettre dans choix le résultat de Obtenir un choix valide()
#       Mettre dans perso choisi le numéro du personnage disponible choisi par le joueur
#       Ajouter une copie du perso choisi à l'équipe
#       Retirer le perso choisi des personnages disponnibles
#   Retourner l'équipe

#Lire les persos()
#   Lire la collection characters dans la base de données
#   Retourner la liste des persos

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