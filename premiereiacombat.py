import classe as cl 
import excecute as ex 
class plateau:pass
etat = plateau()
etat.joueur = 1
etat.Tour = 0

Max = 10**(10)

#initialisation de la grile n*n
def initMap(n):
    L = []
    for i in range(n):
        L.append(n*["Vide"])
    return L   
Map = initMap(10) #grille 10*10

   
Lille = cl.Ville("Lille",1,(0,4))
Map[0][4] = "VJ1 {}".format(Lille.nom)
Paris = cl.Ville("Paris",-1,(9,5))
Map[9][5] = "VJ2 {}".format(Paris.nom)
Lille.production = 10
Paris.production = 10
def updateMap():
    for unite in cl.Unite.list_Unite:
        x,y = unite.coord
        Map[x][y] = Map [x][y] + " " + unite.nom 
        
EclaireurJ1 = cl.Unite.Archer(1,"EclaireurJ1",Lille.coord)
updateMap()
EclaireurJ2 = cl.Unite.Archer(-1,"EclaireurJ2",Paris.coord)
updateMap()

def CoupPossible():
    for unite in cl.Unite.list_Unite:
        unite.directions = ["haut","bas","droite","gauche"]
        for direc in unite.directions:
            if ex.bouge(unite,direc) == "déplacement impossible":
                unite.directions.remove(direc)
                            
                
                
'''                
                
def minmax(etat, profondeur):
    if Lille.PV == 0:
        return (-Max,-1)
    elif Paris.PV == 0:
        return (Max,-1)
    
    elif etat.Tour == 50:
        return (0, -1)
    else:
        scores=[]
        for coup in range(1, 8):
            if coup_possible(etat, coup):
                joue_coup(etat, coup)
                h,_ = minmax(etat, profondeur-1)
                scores.append((h,coup))
                annule_coup(etat, coup)
        if etat.joueur == 1: 
            return max(scores)
        else:
            return min(scores) 

def calcul_heuristique():
    H = 0
    if Lille.PV == 0:
        return -Max
    if Paris.PV == 0:
        return Max
    for unite in cl.Unite.list_Unite:
        H = H + unite.pv * unite.valeur * unite.joueur
    return H
'''
'''
def CommencerPartie1èreVersion(): #à modif plus tard pour + 2 joueurs    
    #j1 = cl.Joueur("J1")
    #j2 = cl.Joueur("J2")

    #T2 = cl.territoire("j1",[(9,5)])
    
    H = calcul_heuristique()
    return H

    #choisir un build pour la ville 1:
H = CommencerPartie1èreVersion()
#ex.affiche(Map)
        
'''
#Heuristique calcul des cases avec la valeur de l'unité * nb pv
'''

def Passe_Tour(): pass                        
 '''           

