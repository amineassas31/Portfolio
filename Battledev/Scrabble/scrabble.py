with open("donnee_scrabble", "r") as fichier:
    liste_score_lettre = fichier.readline()
    contenu = fichier.read().splitlines()
print(liste_score_lettre)
liste_score_lettre = liste_score_lettre.split(" ")

print(liste_score_lettre)
print(contenu)
liste_finale = []
for element in contenu:
    score = 0
    for lettre in element:
        if lettre in liste_score_lettre:
            score += int(liste_score_lettre[liste_score_lettre.index(lettre)+1])
    liste_finale.append(str(score)+element)

liste_finale.sort(reverse=True)
for element in liste_finale:
    print(element[1:])

