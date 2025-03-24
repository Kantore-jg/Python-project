import math
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
#d=float(input("d: "))
perimetre=(a+b+c)
d=perimetre/2
#S=d*(d-a)*(d-b)*(d-c)
aire=math.sqrt(d*(d-a)*(d-b)*(d-c))
print(f"le perimetre est {perimetre} et l'aire est {aire}")