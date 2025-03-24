a=input("saisir le nom: ")
compteur=0
for i in a:
    a1=a[::-1]
    if i=="e":
        compteur+=1
print(f"le nombre de e  dans {a} est {compteur}, l'inverse est {a1}")

