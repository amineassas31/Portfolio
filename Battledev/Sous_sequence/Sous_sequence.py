with open("donnee_Sous_sequence", "r") as fichier:
    t = fichier.read().splitlines()
x = t[0]
y = t[1]
i = 0
j = 0
while i < len(y) and j < len(x):
    if y[i] == x[j]:
        j += 1
    i += 1
if j == len(x):
    print("OK")
else:
    print("NOK {}".format(j))

