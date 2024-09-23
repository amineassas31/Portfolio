with open("donnee_Energie_du_futur", "r") as fichier:
    puissance = fichier.readline()
puissance = int(puissance)
for i in range(0, 4):
    if puissance % 3 == 0:
        puissance //= 3

    elif puissance % 2 == 0:
        puissance //= 2
    else:
        puissance -= 1
print(puissance)
