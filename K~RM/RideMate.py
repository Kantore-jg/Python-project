import random
import tkinter as tk
from tkinter import messagebox

# Données stockées
reservations = []  # Liste pour les réservations
paiements = []     # Liste pour les paiements

# Fonction pour changer de page
def afficher_page(page):
    for frame in frames.values():
        frame.pack_forget()
    frames[page].pack(fill="both", expand=True)


# def afficher_vehicule():
#     tk.Label("Voici la liste de nos véhicules 😍👇🏾 :\n- BMW\n- Voxy\n- Bus\n\nMotos :\n- SUZUKI\n- YAMAHA\n- DT")
#     #messagebox.showinfo("Paiement réussi", f"Paiement enregistré avec succès ! \ud83c\udf89\nCompte : {matricule}\nMontant : {montant}")




# Fonction pour gérer le paiement
def paiement():
    moyen = var_paiement.get()
    if moyen in ["lumicash", "ihela"]:
        matricule = entry_matricule.get()
        password = entry_password.get()
        montant = entry_montant.get()
        paiements.append({"Compte": matricule, "Montant": montant, "Moyen": moyen, "Statut": "En attente"})
        messagebox.showinfo("Paiement réussi", f"Paiement enregistré avec succès ! \ud83c\udf89\nCompte : {matricule}\nMontant : {montant}")
        afficher_page("main")
    else:
        messagebox.showerror("Erreur", "Nous n'acceptons que Lumicash et iHela.")

# Fonction pour enregistrer une réservation
def enregistrer_reservation():
    numero_reservation = random.randint(1000, 9999)
    reservations.append({
        "Numéro": numero_reservation,
        "Destination": entry_destination.get(),
        "Durée": entry_duree.get(),
        "Personnes": entry_personnes.get(),
        "Heure": entry_heure.get(),
        "Statut": "En attente"
    })
    messagebox.showinfo("Réservation réussie", f"Réservation enregistrée \ud83c\udf89\nNuméro : {numero_reservation}")
    afficher_page("paiement")

# Fonction pour confirmer une réservation (Driver)
def confirmer_reservation(reservation):
    reservation["Statut"] = "Acceptée"
    messagebox.showinfo("Confirmation", f"Réservation {reservation['Numéro']} acceptée !")
    afficher_page("driver")
    tk.Button(text="Retour au menu", command=lambda: afficher_page("main")).pack(pady=10)


# Fonction pour refuser une réservation (Driver)
def refuser_reservation(reservation):
    reservation["Statut"] = "Refusée"
    messagebox.showinfo("Refus", f"Réservation {reservation['Numéro']} refusée !")
    afficher_page("driver")

# Fonction pour valider un paiement (Administrateur)
def valider_paiement(paiement):
    paiement["Statut"] = "Confirmé"
    messagebox.showinfo("Paiement confirmé", f"Paiement de {paiement['Montant']} validé.")
    afficher_page("admin")
    tk.Button(text="Retour au menu", command=lambda: afficher_page("main")).pack(pady=10)


# Fonction pour valider une réservation (Administrateur)
def valider_reservation(reservation):
    reservation["Statut"] = "Confirmée"
    messagebox.showinfo("Réservation confirmée", f"Réservation {reservation['Numéro']} confirmée.")
    afficher_page("admin")
    tk.Button(text="Retour au menu", command=lambda: afficher_page("main")).pack(pady=10)


# Initialisation de l'interface principale
root = tk.Tk()
root.title("RideMate")
root.geometry("400x500")

frames = {}

# Page principale
frame_main = tk.Frame(root)
frames["main"] = frame_main

tk.Label(frame_main, text="Welcome to RideMate's services \ud83d\ude97", font=("Arial", 16)).pack(pady=20)

tk.Label(frame_main, text="Inscrivez-vous ici \ud83d\udc47\ud83c\udffe").pack()
tk.Label(frame_main, text="Nom :").pack()
tk.Entry(frame_main).pack()

tk.Label(frame_main, text="Adresse :").pack()
tk.Entry(frame_main).pack()

tk.Label(frame_main, text="Téléphone :").pack()
tk.Entry(frame_main).pack()

tk.Label(frame_main, text="E-mail :").pack()
tk.Entry(frame_main).pack()

tk.Label(frame_main, text="Choisissez votre catégorie :").pack(pady=10)
var_categorie = tk.StringVar(value="Client")
tk.OptionMenu(frame_main, var_categorie, "Client", "Driver", "Administrateur").pack()

def choisir_categorie():
    categorie = var_categorie.get()
    if categorie == "Client":
        # afficher_vehicule()
        afficher_page("reservation")
    elif categorie == "Driver":
        afficher_page("driver")
    elif categorie == "Administrateur":
        afficher_page("admin")
    else:
        messagebox.showerror("Erreur", "Catégorie invalide.")

tk.Button(frame_main, text="Valider", command=choisir_categorie).pack(pady=10)

# Page de réservation
frame_reservation = tk.Frame(root)
frames["reservation"] = frame_reservation

tk.Label(frame_reservation, text="Ajouter la destination \u2708\ufe0f").pack()
entry_destination = tk.Entry(frame_reservation)
entry_destination.pack()

tk.Label(frame_reservation, text="Durée pour le retour \ud83d\udd52").pack()
entry_duree = tk.Entry(frame_reservation)
entry_duree.pack()

tk.Label(frame_reservation, text="Nombre de personnes \ud83d\udc40").pack()
entry_personnes = tk.Entry(frame_reservation)
entry_personnes.pack()

tk.Label(frame_reservation, text="Heure de départ \ud83d\udd52").pack()
entry_heure = tk.Entry(frame_reservation)
entry_heure.pack()

tk.Button(frame_reservation, text="Valider", command=enregistrer_reservation).pack(pady=10)

tk.Button(frame_reservation, text="Retour", command=lambda: afficher_page("main")).pack(pady=10)

# Page de paiement
frame_paiement = tk.Frame(root)
frames["paiement"] = frame_paiement

tk.Label(frame_paiement, text="Choisissez votre moyen de paiement :").pack()
var_paiement = tk.StringVar(value="lumicash")
tk.Radiobutton(frame_paiement, text="Lumicash", variable=var_paiement, value="lumicash").pack()
tk.Radiobutton(frame_paiement, text="iHela", variable=var_paiement, value="ihela").pack()

tk.Label(frame_paiement, text="Numéro de compte").pack()
entry_matricule = tk.Entry(frame_paiement)
entry_matricule.pack()

tk.Label(frame_paiement, text="Mot de passe \ud83d\udd10").pack()
entry_password = tk.Entry(frame_paiement, show="*")
entry_password.pack()

tk.Label(frame_paiement, text="Montant \ud83d\udcb8").pack()
entry_montant = tk.Entry(frame_paiement)
entry_montant.pack()

tk.Button(frame_paiement, text="Payer", command=paiement).pack(pady=10)

tk.Button(frame_paiement, text="Retour", command=lambda: afficher_page("main")).pack(pady=10)

# Page Driver
frame_driver = tk.Frame(root)
frames["driver"] = frame_driver

tk.Label(frame_driver, text="Réservations disponibles :").pack()

def afficher_reservations_driver():
    for widget in frame_driver.winfo_children():
        widget.pack_forget()
    tk.Label(frame_driver, text="Réservations disponibles :").pack()
    for reservation in reservations:
        if reservation["Statut"] == "En attente":
            tk.Label(frame_driver, text=f"Numéro {reservation['Numéro']} - {reservation['Destination']}").pack()
            tk.Button(frame_driver, text="Accepter", command=lambda r=reservation: confirmer_reservation(r)).pack()
            tk.Button(frame_driver, text="Refuser", command=lambda r=reservation: refuser_reservation(r)).pack()

tk.Button(frame_driver, text="Actualiser", command=afficher_reservations_driver).pack(pady=10)

tk.Button(frame_driver, text="Retour", command=lambda: afficher_page("main")).pack(pady=10)
tk.Button(text="menu", command=lambda: afficher_page("main")).pack(pady=10)

# Page Administrateur
frame_admin = tk.Frame(root)
frames["admin"] = frame_admin

def afficher_admin():
    for widget in frame_admin.winfo_children():
        widget.pack_forget()
    tk.Label(frame_admin, text="Paiements enregistrés :").pack()
    for paiement in paiements:
        if paiement["Statut"] == "En attente":
            tk.Label(frame_admin, text=f"Compte : {paiement['Compte']} - Montant : {paiement['Montant']}").pack()
            tk.Button(frame_admin, text="Valider Paiement", command=lambda p=paiement: valider_paiement(p)).pack()
    
    tk.Label(frame_admin, text="\nRéservations enregistrées :").pack()
    for reservation in reservations:
        if reservation["Statut"] == "Acceptée":
            tk.Label(frame_admin, text=f"Numéro {reservation['Numéro']} - {reservation['Destination']}").pack()
            tk.Button(frame_admin, text="Confirmer Réservation", command=lambda r=reservation: valider_reservation(r)).pack()


tk.Button(frame_admin, text="Actualiser", command=afficher_admin).pack(pady=10)
tk.Button(frame_admin, text="Retour", command=lambda: afficher_page("main")).pack(pady=10)
# Initialiser sur la page principale
afficher_page("main")

root.mainloop()
