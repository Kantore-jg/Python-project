nombre=0
count=0
l=[]
while True:
    nombre=input("Veuillez entrer une valeur :")
    if nombre=="":
        break
    try:
        nombre=int(nombre)
        l.append(nombre)
        count+=1
    except ValueError:
        print("entre invalid!!")
print(f"our list is: {l}")
        