import tkinter as tk
from tkinter import messagebox
import random

def afficher_frame(frame):
    """
    Affiche uniquement le frame donné et cache les autres.
    """
    for f in frames.values():
        f.pack_forget()
    frame.pack(fill="both", expand=True)

def valider_paiement():
    moyen = moyen_var.get()
    type_paiement = type_paiement_var.get()

    if not moyen or not type_paiement:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    if type_paiement == "inscription":
        inscrire = inscription_entry.get()
        jeux = jeux_entry.get() or "Aucun jeu"
        recu = f"Argent: {inscrire}\nJeux: {jeux}"
        messagebox.showinfo("Reçu", recu)
    elif type_paiement == "tranche":
        tranche_num = tranche_entry.get()
        montant_tranche = montant_entry.get()
        bordereau = random.randint(1000, 9999)
        recu = f"Tranche: {tranche_num}\nMontant: {montant_tranche}\nBordereau: {bordereau}"
        messagebox.showinfo("Reçu", recu)

def enregistrer_enseignant():
    nom = nom_entry.get()
    cours = cours_entry.get()
    matriculation = matriculation_entry.get()
    credit = credit_entry.get()
    jours = jours_entry.get()

    if not (nom and cours and matriculation and credit and jours):
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    badge = f"Enseignant: {nom}\nCours: {cours}\nMatriculation: {matriculation}\nCrédit: {credit}\nJours disponibles: {jours}"
    messagebox.showinfo("Badge généré", badge)

# Création de la fenêtre principale
root = tk.Tk()
root.title("ITEM's Services")

frames = {}

# Frame principal
frame_menu = tk.Frame(root)
tk.Label(frame_menu, text="Bienvenue aux services ITEM", font=("Arial", 16)).pack(pady=10)
tk.Button(frame_menu, text="Élève", command=lambda: afficher_frame(frames['eleve'])).pack(pady=5)
tk.Button(frame_menu, text="Enseignant", command=lambda: afficher_frame(frames['enseignant'])).pack(pady=5)
tk.Button(frame_menu, text="Administrateur", command=lambda: afficher_frame(frames['admin'])).pack(pady=5)
tk.Button(frame_menu, text="Quitter", command=root.quit).pack(pady=5)
frames['menu'] = frame_menu

# Frame élève
frame_eleve = tk.Frame(root)
tk.Label(frame_eleve, text="Choisissez une faculté", font=("Arial", 14)).pack(pady=10)
for fac in ["GL", "GI", "Télécom", "IG", "IR"]:
    tk.Button(frame_eleve, text=fac, command=lambda f=fac: afficher_frame(frames['paiement'])).pack(pady=5)
tk.Button(frame_eleve, text="Retour", command=lambda: afficher_frame(frames['menu'])).pack(pady=10)
frames['eleve'] = frame_eleve

# Frame paiement
frame_paiement = tk.Frame(root)
tk.Label(frame_paiement, text="Paiement", font=("Arial", 14)).pack(pady=10)

moyen_var = tk.StringVar()
type_paiement_var = tk.StringVar()

# Widgets de paiement
tk.Label(frame_paiement, text="Moyen de paiement:").pack()
tk.OptionMenu(frame_paiement, moyen_var, "IBBM+", "CRDB").pack()

tk.Label(frame_paiement, text="Type de paiement:").pack()
tk.OptionMenu(frame_paiement, type_paiement_var, "inscription", "tranche").pack()

tk.Label(frame_paiement, text="Montant inscription:").pack()
inscription_entry = tk.Entry(frame_paiement)
inscription_entry.pack()

tk.Label(frame_paiement, text="Numéro tranche:").pack()
tranche_entry = tk.Entry(frame_paiement)
tranche_entry.pack()

tk.Label(frame_paiement, text="Montant tranche:").pack()
montant_entry = tk.Entry(frame_paiement)
montant_entry.pack()

tk.Label(frame_paiement, text="Jeux:").pack()
jeux_entry = tk.Entry(frame_paiement)
jeux_entry.pack()

tk.Button(frame_paiement, text="Valider", command=valider_paiement).pack(pady=5)
tk.Button(frame_paiement, text="Retour", command=lambda: afficher_frame(frames['menu'])).pack(pady=5)
frames['paiement'] = frame_paiement

# Frame enseignant
frame_enseignant = tk.Frame(root)
tk.Label(frame_enseignant, text="Enregistrement Enseignant", font=("Arial", 14)).pack(pady=10)

# Widgets pour enseignant
tk.Label(frame_enseignant, text="Nom:").pack()
nom_entry = tk.Entry(frame_enseignant)
nom_entry.pack()

tk.Label(frame_enseignant, text="Cours:").pack()
cours_entry = tk.Entry(frame_enseignant)
cours_entry.pack()

tk.Label(frame_enseignant, text="Matriculation:").pack()
matriculation_entry = tk.Entry(frame_enseignant)
matriculation_entry.pack()

tk.Label(frame_enseignant, text="Crédit:").pack()
credit_entry = tk.Entry(frame_enseignant)
credit_entry.pack()

tk.Label(frame_enseignant, text="Jours disponibles:").pack()
jours_entry = tk.Entry(frame_enseignant)
jours_entry.pack()

tk.Button(frame_enseignant, text="Valider", command=enregistrer_enseignant).pack(pady=5)
tk.Button(frame_enseignant, text="Retour", command=lambda: afficher_frame(frames['menu'])).pack(pady=5)
frames['enseignant'] = frame_enseignant

# Frame administrateur
frame_admin = tk.Frame(root)
tk.Label(frame_admin, text="Administration", font=("Arial", 14)).pack(pady=10)

tk.Button(frame_admin, text="Consulter enseignants", command=lambda: messagebox.showinfo("Info", "Consultation enseignants effectuée.")).pack(pady=5)
tk.Button(frame_admin, text="Consulter étudiants", command=lambda: messagebox.showinfo("Info", "Consultation étudiants effectuée.")).pack(pady=5)
tk.Button(frame_admin, text="Retour", command=lambda: afficher_frame(frames['menu'])).pack(pady=10)
frames['admin'] = frame_admin

# Afficher le menu principal au démarrage
afficher_frame(frames['menu'])
root.mainloop()
