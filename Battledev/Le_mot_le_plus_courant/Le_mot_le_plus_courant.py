with open("donnee_Le_mot_le_plus_courant", "r") as fichier:
    lignes = fichier.read().splitlines()

mots = []

for ligne in lignes:
    mots.append(ligne.split(" "))

liste_mots = []
for mot in mots:
    for element in mot:
        liste_mots.append(element.lower().replace(".", ""))

n_m = []
n = len(lignes)
for mot in liste_mots:
    i = liste_mots.count(mot)
    if i < n and len(mot) > 1:
        n_m.append("{} {}".format(i,mot))
s = set(n_m)
n_m = list(s)
n_m.sort( key=lambda x: (x[2]))

n_m.sort(reverse=True, key=lambda x: (x[0]))

for i in range(3):
    print(n_m[i])



