l=['Jean'
,
'Maximilien'
,
'Brigitte'
,
'Sonia'
,
'Jean-Pierre'
,
'Sandra']
taille=len(l)
l1=[]
l2=[]
compteur=0
while compteur<taille:
    if len(l[compteur])<6:
        l2.append(l[compteur])
        compteur+=1
    elif len(l[compteur])>=6:
        l1.append(l[compteur])
        compteur+=1
print(f"les plus de 6 caracteres sont {l1}\nles moins de 6 caracteres sont {l2}")
