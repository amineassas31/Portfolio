with open("donnee_Economies_de_papier", "r") as fichier:
    liste_hauteur = fichier.readline()

liste_hauteur = liste_hauteur.split(" ")
i = 0
n_page = 0
while i < len(liste_hauteur)-1:

    if int(liste_hauteur[i]) + int(liste_hauteur[i + 1]) <= 10:
        i += 2
    else:
        i += 1
    n_page += 1
    if i == len(liste_hauteur)-1:
        n_page += 1
print(n_page)
