import random
import tkinter as tk
from tkinter import messagebox
import json

# Charger l'historique depuis un fichier JSON
try:
    with open("historique.json", "r") as file:
        historique = json.load(file)
except FileNotFoundError:
    historique = {"reservations": [], "paiements": []}

# Sauvegarder l'historique dans un fichier JSON
def sauvegarder_historique():
    with open("historique.json", "w") as file:
        json.dump(historique, file)

# Fonction pour changer de page
def afficher_page(page):
    for frame in frames.values():
        frame.pack_forget()
    frames[page].pack(fill="both", expand=True)

# Fonction pour afficher l'historique
def afficher_historique():
    for widget in frame_historique.winfo_children():
        widget.pack_forget()

    tk.Label(frame_historique, text="Historique des Activités", font=("Arial", 16)).pack(pady=10)

    if not historique["reservations"] and not historique["paiements"]:
        tk.Label(frame_historique, text="Aucune activité enregistrée.").pack()
    else:
        tk.Label(frame_historique, text="Réservations :", font=("Arial", 14)).pack(pady=5)
        for res in historique["reservations"]:
            tk.Label(frame_historique, text=f"Numéro: {res['Numéro']} | Destination: {res['Destination']} | Statut: {res['Statut']}").pack()

        tk.Label(frame_historique, text="Paiements :", font=("Arial", 14)).pack(pady=5)
        for paiement in historique["paiements"]:
            tk.Label(frame_historique, text=f"Compte: {paiement['Compte']} | Montant: {paiement['Montant']} | Statut: {paiement['Statut']}").pack()

    tk.Button(frame_historique, text="Retour au menu", command=lambda: afficher_page("main")).pack(pady=10)

# Fonction pour gérer le paiement
def paiement():
    moyen = var_paiement.get()
    if moyen in ["lumicash", "ihela"]:
        matricule = entry_matricule.get()
        password = entry_password.get()
        montant = entry_montant.get()

        paiement_data = {
            "Compte": matricule,
            "Montant": montant,
            "Moyen": moyen,
            "Statut": "En attente"
        }
        historique["paiements"].append(paiement_data)
        sauvegarder_historique()

        messagebox.showinfo("Paiement réussi", f"Paiement enregistré avec succès ! \ud83c\udf89\nCompte : {matricule}\nMontant : {montant}")
        afficher_page("main")
    else:
        messagebox.showerror("Erreur", "Nous n'acceptons que Lumicash et iHela.")

# Fonction pour enregistrer une réservation
def enregistrer_reservation():
    numero_reservation = random.randint(1000, 9999)
    reservation_data = {
        "Numéro": numero_reservation,
        "Destination": entry_destination.get(),
        "Durée": entry_duree.get(),
        "Personnes": entry_personnes.get(),
        "Heure": entry_heure.get(),
        "Statut": "En attente"
    }
    historique["reservations"].append(reservation_data)
    sauvegarder_historique()

    messagebox.showinfo("Réservation réussie", f"Réservation enregistrée \ud83c\udf89\nNuméro : {numero_reservation}")
    afficher_page("paiement")

# Initialisation de l'interface principale
root = tk.Tk()
root.title("RideMate")
root.geometry("400x500")
frames = {}

# Page principale
frame_main = tk.Frame(root)
frames["main"] = frame_main
tk.Label(frame_main, text="Welcome to RideMate's services \ud83d\ude97", font=("Arial", 16)).pack(pady=20)
tk.Button(frame_main, text="Voir l'historique des activités", command=afficher_historique).pack(pady=10)
tk.Label(frame_main, text="Inscrivez-vous ici \ud83d\udc47\ud83c\udffe").pack()

# Champs d'inscription
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
tk.Button(frame_reservation, text="Retour au menu", command=lambda: afficher_page("main")).pack(pady=10)

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
tk.Button(frame_paiement, text="Retour au menu", command=lambda: afficher_page("main")).pack(pady=10)

# Page de l'historique
frame_historique = tk.Frame(root)
frames["historique"] = frame_historique

# Charger la page principale
afficher_page("main")
root.mainloop()
