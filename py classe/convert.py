secondes=int(input("saisir le nombre que tu veux convertir: "))
total_secondes=secondes
minute=60
hours=60*minute
days=hours*24
month=30*days
years=12*month

annee=secondes//years#(((((secondes//60)/60)//24)//30)//12)
secondes%=years
mois=secondes//month#((((secondes//60)//60)//24)//30)
secondes%=month
jour=secondes//days#(((secondes//60)//60)//24)
secondes%=days
heures=secondes//hours#((secondes//60)//60)
secondes%=hours
minutes=secondes//minute#(secondes//60)
secondes%=minute
if annee==0:
    print(f"la conversion de {total_secondes} secondes :\nen mois={mois} mois\nen jours={jour} jours\nen heures={heures} heures\nen minutes={minutes} minutes\nen secondes={secondes} secondes")
    if mois==0:
        print(f"la conversion de {total_secondes} secondes :\nen jours={jour} jours\nen heures={heures} heures\nen minutes={minutes} minutes\nen secondes={secondes} secondes")
        if jour==0:
            print(f"la conversion de {total_secondes} secondes :\nen heures={heures} heures\nen minutes={minutes} minutes\nen secondes={secondes} secondes")
            if heures==0:
                print(f"la conversion de {total_secondes} secondes :\nen minutes={minutes} minutes\nen secondes={secondes} secondes")
                if minutes:
                    print(f"la conversion de {total_secondes} secondes :\nen secondes={secondes} secondes")
                    if secondes==0:
                        print(f"la conversion de {total_secondes} secondes : il n'ya pas des annees, ni des mois, jours,heures,... dans 0 secondes")
else:
    print(f"la conversion de {total_secondes} secondes :\nen annee={annee} ans\nen mois={mois} mois\nen jours={jour} jours\nen heures={heures} heures\nen minutes={minutes} minutes")