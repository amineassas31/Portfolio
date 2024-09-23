import random

couleur = ['orange', 'jaune', 'vert', 'rose', 'bleu', 'violet']


def lancer_de(n_lance):
    lances = []
    for i in range(1, n_lance + 1):
        lances.append(random.randint(1, 6))
    return lances


s = lancer_de(10)
somme = sum(s)
somme = (somme % 48) + 1
somme = somme % 6
print(couleur[somme])
