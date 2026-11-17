#Afficher les options à l'écran

#Récupérer un choix valide parmi les options
---#Tant que infini
---    #Afficher les options numérotées
---    #Demander un choix au joueur
---    #Si choix est valide!!!
---        #Retrouner le choix valide
---    #Afficher un message d'erreur

#Choix est valide
    ---#Si le choix du joueur est composé uniquement de chiffres
    ---    #Transformer le choix rentrer par le joueur en nombre entier
    ---    #Si le choix du joueur n'est pas compris dans l'intervalle de choix dispo
    ---        #Afficher un message d'erreur
    ---    #Sinon (choix composé de chiffres et compris dans l'intervalle)
    ---        #Vérifie choix du joueur!!!
    ---#Sinon (choix pas uniquement composé de chiffres)
    ---    #Afficher un message d'erreur

#Vérifie choix du joueur
    #Si le choix du joueur est égal à 1
        #Lancer le jeu!!!
    #Si le choix du joueur est égal à 2
        #Afficher le tableau des scores!!!
    #Si le choix du joueur est égal à 3
        #Quitter le programme