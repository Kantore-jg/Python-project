a = int(input("Saisir un nombre: "))
if a % 2 == 0:
    print(f"Le nombre {a} est pair!")
else:
    print(f"Le nombre {a} est impair!")

fact = 1  
if a < 0:
    print("La factorielle n'existe pas pour les nombres négatifs.")
elif a == 0:
    print(f"La factorielle de 0 est 1.")
else:
    for i in range(1, a + 1): 
        fact *= i
    print(f"La factorielle de {a} est {fact}.")
