equipe={"kantore":"developpeur des app en py","Carlos":"Developpeur des app en java","Wonder":"chef d'equipe de developpeurs des logiciels"}
research=input("entrer le mot que tu veux rechercher: ").lower()
for i in  equipe:
    if research==i:
        print(equipe[research])
        break
print("desole votre mot n'a pas dans le dictionnaire")
