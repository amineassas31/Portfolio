with open("donnee_Plus_petit_rectangle", "r") as fichier:
    n = fichier.readline()
    cordonnee = fichier.read().splitlines()

cordonnee1 = []
for element in cordonnee:
    cordonnee1.append(element.split(" "))
cordonneex = []
cordonneey = []
for element in cordonnee1:
    cordonneex.append(int(element[0]))
    cordonneex.append(int(element[2]))
    cordonneey.append(int(element[1]))
    cordonneey.append(int(element[3]))
print(min(cordonneex), min(cordonneey), min(cordonneex), max(cordonneey), max(cordonneex), min(cordonneey),
      max(cordonneex), max(cordonneey), )
