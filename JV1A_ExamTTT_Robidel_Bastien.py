ligne_1 = ["1", "2", "3"]
ligne_2 = ["4", "5", "6"]
ligne_3 = ["7", "8", "9"]
grille = [ligne_1, ligne_2, ligne_3]

def grille_jeu(mytab):
    for i in range(len(mytab)):
        print(mytab[i])

def tour(mytab, nb_tours):
    joueur = "X"
    emplacement = str(input("Sur quelle case veux-tu jouer?"))
    for i in range(len(ligne_1)):
        if ligne_1[i] == emplacement and ligne_1[i] != "O" and ligne_1[i] != "X":
            ligne_1[i] = joueur
    for j in range(len(ligne_2)):
        if ligne_2[j] == emplacement and ligne_2[j] != "O" and ligne_2[j] != "X":
            ligne_2[j] = joueur
    for k in range(len(ligne_2)):
        if ligne_3[k] == emplacement and ligne_3[k] != "O" and ligne_3[k] != "X":
            ligne_3[k] = joueur

    if joueur == "X":
        joueur = "O"
    else:
        joueur = "X"

    for l in range(len(mytab)):
        print(mytab[l])

def aligner(mytab):
    i,j,k = 0,0,0
    alignement = False
    for l in range(len(mytab)):
        if mytab[i][j] == mytab[i][j+1] and mytab[i][j] == mytab[i][j+2]:
            alignement = True
    if mytab[i][k] == mytab[i+1][k] and mytab[i][k] == mytab[i+2][k]:
        alignement = True
    if mytab[i][k] == mytab[i+1][k+1] and mytab[i][k] == mytab[i+2][k+2]:
        alignement = True
    if mytab[i+2][k] == mytab[i+1][k+1] and mytab[i][k] == mytab[i][k+2]:
        alignement = True
    return alignement

def grille_complete(nb_tours):
    complete = False
    if nb_tours == 9:
        complete = True
    return complete




def Tic_tac_Toe():
    ligne_1 = ["1", "2", "3"]
    ligne_2 = ["4", "5", "6"]
    ligne_3 = ["7", "8", "9"]
    grille = [ligne_1, ligne_2, ligne_3]
    victoire = False
    nb_tours = 0
    while aligner == False and grille_complete == False:
        tour(grille, nb_tours)
        nb_tours +=1
        victoire = aligner(grille)
        grillepleine = grille_complete(nb_tours)
    if aligner == True:
        print('Bravo !!')
    if grille_complete == True:
        print("Vous ferez mieux la prochaine fois !")
    return 

print(Tic_tac_Toe())

# pour coder un jeu de puissanc 4 il faudra augmenter la taille de la grille, changer les "X" et "O" par, par exemple "R" et "J", modifier les conditions de victoire pour que l'on gagne si l'on aligne 4 symbole et non 3. modifier la fonction de la grille complete pour augmenter le nombre de tours