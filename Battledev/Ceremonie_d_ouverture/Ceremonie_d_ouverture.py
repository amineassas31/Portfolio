with open("donnee_Ceremonie_d_ouverture", "r") as fichier:
    n_delegation = fichier.readline()
    delegation = fichier.read().splitlines()

info_delegation = []
for element in delegation:
    info_delegation.append(element.split(" "))

delegation = []
for element in info_delegation:
    delegation.append([int(element[1]) / int(element[2]), element[0]])
maximum = max(delegation)
print(maximum[1])


