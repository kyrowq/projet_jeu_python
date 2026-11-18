#Afficher le menu()
#   Afficher l'option 1: Lancer le jeu
#   Afficher l'option 2: Tableau des scores
#   Afficher l'option 3: Quitter le jeu

#Vérifier si le choix est valide()
#   Si ce n'est pas un digit
#       Retourne FAUX
#   Convertir le choix du joueur en entier
#   Si le choix du joueur est inférieur au minimum ou supérieur au maximum
#       Retourne FAUX
#   Retourne VRAI

#Obtenir un choix valide()
#   Tant que infini
#       Afficher le menu()
#       Demander au joueur son choix
#       Si le choix est valide()
#           Retourner le choix du joueur
#       Afficher une erreur

#Executer le choix()
#   Selon le choix
#       choix 1: Lancer le jeu()
#       choix 2: Afficher les scores()
#       choix 3: Quitter le jeu()

#Lancer le jeu()
#   Composer l'équipe()
#   Initialiser le numéro de la manche à 1
#   Tant qu'il reste au moins un personnage de l'équipe en vie
#       Créer les monstres de la manche()
#       Combat()
#       Si tous les personnages sont morts
#           Sortir de la boucle
#       Afficher que la manche a été gagné
#       Ajouter 1 au numéro de la manche
#   Afficher la fin de partie avec le nombre de manche atteinte
#   Enregistrer le score()