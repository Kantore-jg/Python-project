class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.__age = age  # Attribut privé

    def presentation_personne(self):
        print(f"Bonjour, je suis {self.nom} {self.prenom}")

    def affiche_age(self):
        return self.__age

class Travailleur(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

# Création de 3 personnes
personne1 = Personne("Gaston", "Niyonkuru", 30)
personne2 = Personne("Aline", "Mukamana", 25)
personne3 = Travailleur("Jean", "Habimana", 40, "TR123")

# Conversion de personne1 en travailleur
travailleur1 = Travailleur(personne1.nom, personne1.prenom, personne1.affiche_age(), "TR124")

# Conversion de personne2 en travailleur
travailleur2 = Travailleur(personne2.nom, personne2.prenom, personne2.affiche_age(), "TR125")

# Affichage des présentations
personne1.presentation_personne()
personne2.presentation_personne()
personne3.presentation_personne()

# Affichage des âges
print(f"Age de {personne1.nom}: {personne1.affiche_age()} ans")
print(f"Age de {personne2.nom}: {personne2.affiche_age()} ans")
print(f"Age de {personne3.nom}: {personne3.affiche_age()} ans")

# Affichage des travailleurs
print(f"Travailleur 1: {travailleur1.nom} {travailleur1.prenom}, Matricule: {travailleur1.matricule}")
print(f"Travailleur 2: {travailleur2.nom} {travailleur2.prenom}, Matricule: {travailleur2.matricule}")
