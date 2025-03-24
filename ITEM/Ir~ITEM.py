import random

print("Bienvenue chez ITEM's Services")
print("-----------------------------")

def paiement(faculte):
    """
    Fonction pour gérer le paiement.
    """
    moyen = input("Choisir le moyen de paiement entre IBBM+ et CRDB: ").upper()
    if moyen in ["IBBM+", "CRDB"]:
        type_paiement = input("L'inscription ou tranche?: ").lower()
        if type_paiement == "inscription":
            inscrire = input("Entrez le montant pour l'inscription: ")
            jeux = input("Indiquez un jeu que vous jouez (laissez vide si aucun): ")
            if not jeux:
                jeux = "Aucun jeu"
            recu = f"Argent: {inscrire}\nFaculté: {faculte}\nJeux: {jeux}"
            print("Reçu généré:\n", recu)
        elif type_paiement == "tranche":
            tranche_num = input("Entrez le numéro de la tranche: ")
            montant_tranche = input("Entrez le montant pour cette tranche: ")
            bordereau = random.randint(1000, 9999)
            recu = f"Tranche: {tranche_num}\nPaiement: {montant_tranche}\nFaculté: {faculte}\nBordereau: {bordereau}"
            print("Reçu généré:\n", recu)
        else:
            print("Type de paiement invalide.")
    else:
        print("Moyen de paiement invalide.")

def eleve():
    """
    Fonction principale pour la catégorie élève.
    """
    print("Facultés disponibles à ITEM:\n----------------------------")
    print("1. GL\n2. GI\n3. Télécom\n4. IG\n5. IR")
    fac = input("Choisissez la faculté que vous voulez apprendre: ").upper()
    if fac in ["GL", "GI", "TELECOM", "IG", "IR"]:
        print("Les matériels nécessaires:")
        if fac in ["GL", "GI", "IG"]:
            print("1. PC\n2. Smartphone ou tablette\n3. Bloc-notes")
        elif fac == "TELECOM":
            print("1. Smartphone ou tablette\n2. Bloc-notes")
        # Ajout des détails spécifiques pour chaque faculté
        print("Minerval: 670,000 Fbu/an (4 tranches de 170,000 Fbu chacune)" if fac in ["GL", "GI", "IG"] else "Minerval: 600,000 Fbu/an (4 tranches de 150,000 Fbu chacune)")
        paiement(fac)
    else:
        print("Faculté invalide.")

def enseignant():
    """
    Fonction principale pour la catégorie enseignant.
    """
    nom = input("Nom de l'enseignant: ")
    cours = input("Saisir le cours que vous allez enseigner: ")
    matriculation = input("Matriculation: ")
    credit = input("Crédit du cours: ")
    jours = input("Indiquez les jours disponibles pour enseigner: ")
    badge = f"Enseignant: {nom}\nCours: {cours}\nMatriculation: {matriculation}\nCrédit: {credit}\nJours disponibles: {jours}"
    print("Badge généré:\n", badge)

def administrateur():
    """
    Fonction principale pour la catégorie administrateur.
    """
    cat = input("Voulez-vous consulter les enseignants ou les étudiants?: ").lower()
    if cat == "enseignants":
        print("Consultation des enseignants...")
    elif cat == "étudiants":
        print("Consultation des étudiants...")
    else:
        print("Choix invalide.")

# Programme principal
nom = input("Nom: ")
numero = input("Numéro: ")
email = input("E-mail: ")
categorie = input("Choisissez votre catégorie:\n1. Élève\n2. Enseignant\n3. Administrateur\nVotre choix: ").lower()

if categorie == "1":
    eleve()
elif categorie == "2":
    enseignant()
elif categorie == "3":
    administrateur()
else:
    print("Catégorie invalide.")
