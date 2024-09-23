with open("donnee_Le_jeu_de_la_vie", "r") as fichier:
    n_rectangles = fichier.readline().splitlines()
    rectangles = fichier.read().splitlines()
n_rectangles = int(n_rectangles[0])
# print(n_rectangles)
print(rectangles)
cordonnee_rectangles = []
for rectangle in rectangles:
    t = rectangle.split(" ")
    cordonnee_rectangles.append([int(t[0]), int(t[1])])
    cordonnee_rectangles.append([int(t[2]), int(t[3])])
temp = 0
while pow(10, 6) > len(cordonnee_rectangles) > 0:
    for point in cordonnee_rectangles:
        if [point[0] - 1, point[1] - 1] in cordonnee_rectangles:
            cordonnee_rectangles.append([point[0], point[1] - 1])
        if [point[0], point[1] + 1] not in cordonnee_rectangles or [point[0] - 1, point[1]] not in cordonnee_rectangles:
            cordonnee_rectangles.remove(point)
        temp += 1
if len(cordonnee_rectangles) == pow(10, 6):
    print(-1)
else:
    print(temp)
