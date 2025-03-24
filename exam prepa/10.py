a=input("saisir le mot: ")
count=0
taille=len(a)
while count<taille:
    a1=a[count]+"*"
    count+=1
    print(a1,end="")