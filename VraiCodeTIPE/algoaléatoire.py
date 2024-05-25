from classenaive import Lille,Paris
from executenaif import case_plateau
import classenaive as clna
import executenaif as ex
import random as rd

nombreunite = 0
directions = ["haut", "droite", "bas", "gauche"]
type_unit = ["archer","eclaireur","guerrier"]




# Initialisation de la grille n*n
def init_map(n):
    plateau = []
    for i in range(n):
        plateau.append([])
        for j in range(n):
            plateau[i].append(str((i,j)))
            case_plateau[(i,j)] = True
    return plateau 
            
            
    #return [['' for _ in range(n)] for _ in range(n)]

Map = init_map(10)  # Grille 10*10


Map[0][4] = f"VJ1 {Lille.nom}"
Map[9][5] = f"VJ2 {Paris.nom}"


def update_map():
    Mapaffiche = [row[:] for row in Map]  # Copie profonde de la grille
    for unite in clna.Unite.list_Unite:
        x, y = unite.coord
        Mapaffiche[x][y] = f"{Map[x][y]} {unite.nom}"
    ex.affiche(Mapaffiche)
   
EclaireurJ1 = clna.Unite(1,"eclaireur", "J1,E"+ str(nombreunite) , Lille.coord)
ex.differentunite[EclaireurJ1.nom] = EclaireurJ1
nombreunite += 1
EclaireurJ2 = clna.Unite(-1,"eclaireur", "J-1,E"+ str(nombreunite) , Paris.coord)
ex.differentunite[EclaireurJ2.nom] = EclaireurJ2
nombreunite += 1



def partie_terminée(nbtour):
    if nbtour == 500:
        return False
    if Lille.PV <= 0 or Paris.PV <= 0:
        return False
    return True

def passer_tour(nbtour, joueurquijoue):
    return nbtour + 1, joueurquijoue * -1

def choisir_coup_ia(coups_possibles):
    coup = rd.choice(coups_possibles)
    return coup

def coups_possibles(joueur):
    coups_possibles = ["rien"]
    #coup de formation des unités 
    
    if ex.emplacement_libre(joueur):
        for tu in type_unit:
            coups_possibles.append("forme + " + str(tu))
    
    #determination du joueur
    if joueur == 1:
        listeunité = clna.Unite.list_Unite_joueur1
        liste_unit_ennemie = clna.Unite.list_Unite_joueur2
    elif joueur == -1:
        listeunité = clna.Unite.list_Unite_joueur2
        liste_unit_ennemie = clna.Unite.list_Unite_joueur1    
    #évaluation des chemins possible
    for unite in listeunité:
        x1,y1 = unite.coord
        for uniteattaque in liste_unit_ennemie:
            x2,y2 = uniteattaque.coord
            if unite.portee >= int(((x1-x2)**2+(y1-y2)**2)**(1/2)):
                coups_possibles.append("mouvement + " + unite.nom + " + rien + " + str(uniteattaque.nom) )
        #if unite.pm > 0:
        for direction in directions:
            if ex.bouge(unite,direction) != "déplacement impossible":
                coups_possibles.append("mouvement + " + unite.nom + " + " + str(direction) + " + rien")
    return coups_possibles


def execute_action(action):
    global nombreunite
    #exemple action pour formation "joueur + forme + A"
    if "forme" in action:
        mots = action.split(" + ")
        if int(mots[0]) == -1:
            joueur = -1
        else: 
            joueur = 1
        former = ex.creer_unite(joueur,mots[2],"J"+mots[0]+","+mots[2]+ str(nombreunite))
        nombreunite += 1
        ex.differentunite[former.nom] = former
    #exemple action pour mouvement ou attaque "joueur + mouvement + nomunite + direction + uniteattaqué"
    elif "mouvement" in action:
        mots = action.split(" + ")
        unite_source = ex.differentunite[mots[2]]
        
        if mots[3] != "rien":
            ex.bouge(unite_source,mots[3])
        if mots[4] != "rien":
            unite_cible = ex.differentunite[mots[4]]
            ex.attaquer(unite_source,unite_cible)
    else:
        pass
            
def demander_action():
    while True:
        choix = input("Voulez-vous former une unité (f) ou effectuer un mouvement/une attaque (m) ? ").lower()
        if choix == "f":
            type_unite = input("Entrez le type de l'unité à former : ")
            return f"forme + {type_unite}"
        elif choix == "m":
            nom_unite = input("Entrez le nom de l'unité à déplacer : ")
            direction = input("Entrez la direction : ")
            unite_attaquee = input("Entrez le nom de l'unité à attaquer : ")
            return f"mouvement + {nom_unite} + {direction} + {unite_attaquee}"
        elif choix == "rien":
            return "rien"
        else:
            print("Choix invalide. Veuillez entrer 'f' pour former une unité ou 'm' pour effectuer un mouvement/une attaque.")            
            
# Initialisation des variables de jeu
nbtour = 1
joueurquijoue = 1
profondeur = 2

# Boucle de jeu
while partie_terminée(nbtour): #????
    
    if nbtour > 500:
        break
    
    #update_map()
    if joueurquijoue == 1:
        print(joueurquijoue)
        # Tour de l'IA (joueur 1)
        coup_ia = choisir_coup_ia(coups_possibles(joueurquijoue))
        print(coup_ia)
        execute_action(str(joueurquijoue) + " + " + coup_ia)
        
        nbtour, joueurquijoue = passer_tour(nbtour, joueurquijoue)
    if joueurquijoue == -1:
        # Tour de l'IA (joueur 1)
        print(joueurquijoue)
        coup_ia = choisir_coup_ia(coups_possibles(joueurquijoue))
        print(coup_ia)
        execute_action(str(joueurquijoue) + " + " + coup_ia)
        
        nbtour, joueurquijoue = passer_tour(nbtour, joueurquijoue)
        
        
        ''' 
        # Tour du joueur humain (joueur -1)
        # Attendre l'entrée du joueur humain
        # Effectuer les actions du joueur humain
        # Mettre à jour la position du jeu
        ordre = demander_action()
        
        execute_action(str(joueurquijoue) + " + " + ordre)
        
        nbtour, joueurquijoue = passer_tour(nbtour, joueurquijoue)  
        ''' 
        
        
print("partie terminée match nul")





