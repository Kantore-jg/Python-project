from turtle import*
def carre(taille,couleur):
    color(couleur)
    c=0
    while c<4:
        forward(taille)
        right(90)
        c=c+1
carre(200,'pink')
carre(200,'red')
carre(200,'green')
carre(200,'yellow')
carre(200,'blue')
carre(200,'black')
