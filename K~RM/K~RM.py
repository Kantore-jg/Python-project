import random

# Introduction
print("K~RM")
print("Welcome to RideMate's services!")
print("S'inscrire ici👇🏾:")

# Inscription
nom = input("Nom 😀 : ")
adresse = input("Adresse 🗺️ : ")
telephone = input("Téléphone 📱 : ")
email = input("E-mail 🖥️ : ")

print(f"Welcome again {nom} at RideMate's service!")
categorie=0
# Choix de catégorie
while(categorie<5):
    categorie = int(input(
        "Choisissez votre catégorie dans RideMate entre 👇🏾\n1.Administrateur\n2.Client\n3.Driver\n\n4.quitter\nChoix : ").lower())

    if categorie == 2:
        print("\n--- Connexion Client ---")
        choix = input("Tapez 1 pour voir les véhicules ou 0 pour faire une réservation : ")

        if choix == "1":
            print("Voici la liste de nos véhicules 😍👇🏾 :\n- BMW\n- Voxy\n- Bus\n\nMotos :\n- SUZUKI\n- YAMAHA\n- DT")

            vehicule=input("dites nous de quel vehicule vous aimeriez prendre votre voyage avec eux: ")
            print(f"Merci!, le vehicule {vehicule} sera disponible")
            reserver = input("Voulez-vous faire une réservation ? (oui/non) : ").lower()

            if reserver == "oui":
                destination = input("Ajouter la destination ✈️ : ")
                duree = input("Durée pour le retour 🕒 : ")
                personnes = input("Nombre de personnes 👀 : ")
                heure = input("Heure de départ 🗣️ : ")

                # Générer un numéro de réservation aléatoire
                numero_reservation = random.randint(1000, 9999)

                print(f"\nFélicitations ! Votre réservation a été enregistrée avec succès.")
                print(f"Destination : {destination}")
                print(f"Durée de retour : {duree}")
                print(f"Nombre de personnes : {personnes}")
                print(f"Heure de départ : {heure}")
                print(f"Votre numéro de réservation est : {numero_reservation}")
            else:
                print("RideMate pour vous servir 24h/24 ! 😊")

        elif choix == "0":
            # Réservation directe
            destination = input("Ajouter la destination ✈️ : ")
            duree = input("Durée pour le retour 🕒 : ")
            personnes = input("Nombre de personnes 👀 : ")
            heure = input("Heure de départ 🗣️ : ")

            numero_reservation = random.randint(1000, 9999)

            print(f"\nFélicitations ! Votre réservation a été enregistrée avec succès.")
            print(f"Destination : {destination}")
            print(f"Durée de retour : {duree}")
            print(f"Nombre de personnes : {personnes}")
            print(f"Heure de départ : {heure}")
            print(f"Votre numéro de réservation est : {numero_reservation}")

    # Paiement
        print("\n--- Paiement ---")
        moyen = input("Choisissez votre moyen de paiement :\n1. Lumicash\n2. iHela\nChoix : ").lower()

        def paiement():
            if moyen == "lumicash":
                matricule = input("Saisir le numéro de compte : ")
                password = input("Mot de passe 🔐 : ")
                montant = input("Saisir le montant 💸 : ")
                print(f"\nPaiement enregistré avec succès ! 🎉")
                print(f"Compte : {matricule}\nMontant : {montant}")
            elif moyen == "ihela":
                matricule = input("Saisir le numéro de compte : ")
                password = input("Mot de passe 🔐 : ")
                montant = input("Saisir le montant 💸 : ")
                print(f"\nPaiement enregistré avec succès ! 🎉")
                print(f"Compte : {matricule}\nMontant : {montant}")
            else:
                print("Oups... Nous n'acceptons que Lumicash et iHela.")

        paiement()

    elif categorie == 3:
        print("\n--- Interface Driver ---")
        print("Voir les réservations :")
        print("Pas de réservations pour le moment.")

    elif categorie == 1:
        print("\n--- Interface Administrateur ---")
        action = input("Tapez 'p' pour voir les paiements ou 'r' pour voir les réservations : ").lower()
        if action == "p":
            print("Affichage des paiements enregistrés... 📋")
        elif action == "r":
            print("Affichage des réservations enregistrées... 📋")
        else:
            print("Option invalide.")
    elif categorie==4:
        def quit_program():
            print("you'are welcome")
            exit()
        quit_program()

    else:
        print("plz saisir le nombre qui appartient dans les choix donner")