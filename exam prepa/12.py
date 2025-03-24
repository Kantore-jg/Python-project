list=[32, 5, 12, 8, 3, 75, 2, 15]
taille=len(list)
list1=[]
list2=[]
compteur=0
while compteur<taille:
    if list[compteur]%2==0:
        list2.append(list[compteur])
        compteur+=1
    elif list[compteur]%2!=0:
        list1.append(list[compteur])
        compteur+=1
print(f"les paires sont {list2}\nles impaires sont {list1}")
