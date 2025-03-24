# compteur=0
# a=1
# while compteur<1689:
#     a=a*2
#     b=a*1.65
#     compteur+=1
#     print(f"{a} euros = {b} dollars")
# Initialiser les variables
# Définir les constantes
MULTIPLICATEUR = 2
TAUX_DE_CHANGE = 1.65
NOMBRE_ITERATIONS = 1689

compteur = 0
euros = 1

# Boucle pour multiplier la valeur
while compteur < NOMBRE_ITERATIONS:
    euros *= MULTIPLICATEUR
    dollars = euros * TAUX_DE_CHANGE
    compteur += 1

# Afficher le résultat
print(f"{euros} euros = {dollars} dollars")
