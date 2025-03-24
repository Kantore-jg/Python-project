class Bac2:
    def __init__ (self,genre: bool,nom_fac: str="",name: str="",age: int=0):
        self.genre=genre
        self.nom_fac=nom_fac
        
        self.name=name
        self.age=age
        if nom_fac=="":
            self.demande_nom()
        print("la classe "+nom_fac)

    def etudiant(self):
        
        info_personne="hey i'm "+self.name+" from " +self.nom_fac
        
        
        if self.genre:
            if self.age!=0:
                print(info_personne+ " i'm "+str(self.age)+"years")
            else:
        
                print(info_personne)
            print("genre=masculin")
        if self.age!=0:
            if self.ESTmajeur():
                print("je suis majeur")
            else:
                print("je suis mineur")
        else:
                print(info_personne+ " i'm "+str(self.age)+"years")
           
                print("genre=masculin")
        if self.age!=0:
            if self.ESTmajeur():
                print("je suis majeur")
            else:
                print("je suis mineur")
        print()
           
        
        

    def ESTmajeur(self):
        # print("il a "+self.age)
        return self.age>=18
        #     return True
        # return False
    def demande_nom(self):
        self.nom_fac=input("taper le nom :")
       
personne1=Bac2(True, "info","gildas",0)
personne2=Bac2(False,"genie info","aime",30)
personne3=Bac2(True)
personne4=Bac2(True, age=20)

personne1.etudiant()
personne2.etudiant()
personne4.etudiant()
personne3.etudiant()
# print("est majeur ", personne1.ESTmajeur())




# print("est majeur ", personne2.ESTmajeur())
        