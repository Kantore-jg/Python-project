#Lists
t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octoble', 'novembre', 'decembre']
taille_t1=len(t1)
taille_t2=len(t2)
compteur=0
t3=[]
while compteur<taille_t1:
    t3.append(t2[compteur])
    t3.append(t1[compteur])
    compteur+=1
print(t3)