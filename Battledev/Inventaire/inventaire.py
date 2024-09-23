with open("donnee_inventaire", "r") as fichier:
    n_article = fichier.readline()
    articles = fichier.read().splitlines()
article2 = []
for article in articles:
    article2.append(article.split(" "))
articles = []
for article in article2:
    articles.append([article[0], int(article[1])])
article2 = {}
for article in articles:
    article2[article[0]] = articles.count(article) * article[1]
x = max(article2.values())
for article in article2:
    if article2[article] == x:
        print(article)


