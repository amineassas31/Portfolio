with open("donnee_blockchain", "r") as fichier:
    p = int(fichier.readline())
    n = int(fichier.readline())
    ecriture = fichier.read().splitlines()
majorite = p // 2 + p % 2
ecriture1 = []
for line in ecriture:
    ecriture1.append(line.split(" "))
ecriture = []
for line in ecriture1:
    ecriture.append([line[0], int(line[1])])
livre = ""
for x in ecriture:
    if x[1] >= majorite:
        livre += x[0]
print(livre)
