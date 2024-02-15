
class Humain : 

    humains_crees=0
    all=[] #liste qui va contenir toutes les informations sur les humains quu'on va créer dans le futur

    def __init__(self,c_nom: str, c_age: int, c_taille: int):
        #Assertions à lever
        assert c_age>=0, f"{c_age} est un nombre négatif, veuillez entrer une valeur positive"

        #Affectation des attributs
        self.__nom = c_nom
        self.age = c_age
        self.taille=c_taille
        
        #Actions à exécuter
        Humain.humains_crees+=1
        Humain.all.append(self) 

    def parler(self, message) :
        print("{} : {}".format(self.nom, message))

    @classmethod
    def instantiate_from_csv(cls):
        with open("./humans.csv","r") as fic:
            reader=csv.DictReader(fic)
            humains = list(reader)

        for humain in humains:
            humain = Humain(humain.get("name"), int(humain.get("age")),int(humain.get("taille")))
     
    @classmethod 
    def reinitialisation(cls) :
        Humain.humains_crees=0

  

    """def _getage(self) :
        if(self._age<=1) :
            return str(self._age)+" an"
        else :
            return str(self._age) +" ans"  """
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, c_nom: str):
        self.__nom = c_nom
    
    def __repr__(self) -> str:
        return f"Human:('{self.nom}','{self.age}',{self.taille})"
        
    
    #age = property(_getage)