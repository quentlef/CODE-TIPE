 #Classe Joueur


class Ville:
    list_villes = []
    PV = 400
    etat = "en vie"
    def __init__(self, nom, joueur, coord):
        self.nom = nom
        self.joueur = joueur
        self.coord = coord
        Ville.list_villes.append(self)
        
Lille = Ville("Lille", 1, (0,4))
Paris = Ville("Paris", -1, (9,5))

class Unite:
    list_Unite = []
    list_Unite_joueur1 = []
    list_Unite_joueur2 = []
    directions = ["haut","bas","droite","gauche"]
    
    def __init__(self,joueur,type_u, nom,coord =(1,1)):
          # Attributs d'instance propres à chaque instance
          if type_u == "guerrier":
              self.degats = 20
              self.portee = 1
              self.pm = 2
              self.pv = 50
          if type_u == "eclaireur":   
              self.degats = 10
              self.portee = 1
              self.pm = 3
              self.pv = 50
          if type_u == "archer":    
              self.degats = 15
              self.portee = 2
              self.pm = 2
              self.pv = 50
          self.type_u = type_u    
          self.nom = nom     
          self.coord = coord
          self.joueur = joueur
          #if joueur == 1:
              #Unite.list_Unite_joueur1.append(self)
          #if joueur == -1:
              #Unite.list_Unite_joueur2.append(self)
          Unite.list_Unite.append(self)
    
