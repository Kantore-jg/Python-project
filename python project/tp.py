a=int(input("saisir le nombre: "))
if (a%2==0):
    print(f"le nombre {a} est paire!")
else:
    print(f"le nombre {a} est impaire!")
#i=1
for i in range(1,a):
#while i<a:
    fact=i*a
    i=i+1
print(f"son factoriel est {fact}")
