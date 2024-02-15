#coding:utf-8
import csv
from humain import Humain
  

class Ingenieur(Humain) : 
    all=[]
    def __init__(self, c_nom:str, c_age:int, c_taille:int, domaine:str):
        Humain.__init__(self,c_nom, c_age, c_taille)
        self.domaine = domaine
        Ingenieur.all.append(self)

    def inventer(self) :
        print("L'ingenieur {} en {} invente...".format(self.nom, self.domaine))

#Programme principal
Humain.instantiate_from_csv()

ben = Ingenieur("Kryptonium", 19,186,"Robotique")
print("{} a {}  et {} cm\nAnd {} human(s) created".format(ben.nom, ben.age,ben.taille, Humain.humains_crees))

cen = Humain("Youssouf", 16,175)
print("{} a {}  et {} cm\nAnd {} human(s) created".format(cen.nom, cen.age,cen.taille, Humain.humains_crees))
cen.parler("Je parle bien Francais")
ben.inventer()

print("Nombre total d'êtres humains : {}".format(Humain.humains_crees))
print(isinstance(ben,Humain))

print(Humain.all)
print(Ingenieur.all)
