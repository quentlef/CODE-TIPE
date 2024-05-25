import random as rd
import tkinter as tk 
import classenaive as clna

case_plateau = {}
differentunite = {}

#Crée une liste de liste 10*10 qui va se comporter comme une grille avec des coordonnés (colonne,ligne)
def randomMap(Map):
    n = len(Map)
    for i in range(n):
        for j in range(n):
            random = rd.random()
            if 0 <= random < 0.50 :
                Map[i][j] = "P {}".format((i,j)) #attention type != string, type <class 'str'>      
            elif 0.50<= random < 0.60 :
                Map[i][j] = "M {}".format((i,j))
            elif 0.60 <= random <= 1:
                Map[i][j] = "C {}".format((i,j))
            else:
                print("marche pas")  
    return Map

def affiche(Map):

    for i in range(len(Map)):
        print(Map[i])
    fenetre = tk.Tk()
    Bgcolour = ""
    p = tk.PanedWindow(fenetre, orient=tk.HORIZONTAL)
    p.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)
    n = len(Map)
    for i in range(n):
        m = tk.PanedWindow(p, orient=tk.VERTICAL)
        p.add(m)
        for j in range(n):
            if 'VJ1' in (" " + Map[i][j] + " ") :
                Bgcolour = 'blue'
            elif 'VJ2' in (" " + Map[i][j] + " ") :
                Bgcolour = 'red'
            elif 'P' in (" " + Map[i][j] + " "): 
                Bgcolour = 'green'    
            elif 'M' in (" " + Map[i][j] + " "):
                Bgcolour = 'grey'
            elif 'C' in (" " + Map[i][j] + " ") :
                Bgcolour = 'orange'
            
            else :
                Bgcolour = 'white'
                
            m.add(tk.Label(m, text=(Map[i][j]), background=Bgcolour, anchor=tk.CENTER, relief=tk.RAISED, height=5,width=15))
    p.add(tk.Button(p, text="Quit", command=fenetre.destroy))
    p.pack()
    
    fenetre.mainloop()
    
def copie_unite(unite):
    nouvelle_unite = clna.Unite(unite.joueur,unite.joueur,unite.type_u,unite.nom,unite.coord)
    nouvelle_unite.pv = unite.pv
    return nouvelle_unite

def copie_plateau(plateau):
    nouveau_plateau = plateau.copy()
    return nouveau_plateau
    
type_unit = ["archer","eclaireur","guerrier"]

def creer_unite(joueur, type_unite, nom):
    if joueur == 1:
        coord = clna.Ville.list_villes[0].coord
    elif joueur == -1:
        coord = clna.Ville.list_villes[1].coord
    else:
        raise ValueError("Joueur non valide.")
    if emplacement_libre(joueur) == False:
        return "Emplacement non valide"
    elif type_unite not in type_unit:
            raise ValueError("type non valide.")
    else:
        unite = clna.Unite(joueur,type_unite, nom, coord)
    if joueur == 1:
        clna.Unite.list_Unite_joueur1.append(unite)
    if joueur == -1:
        clna.Unite.list_Unite_joueur2.append(unite)
    return unite

def emplacement_libre(joueur):
    if joueur == 1:
        return case_plateau[clna.Lille.coord]
    elif joueur == -1:
        return case_plateau[clna.Paris.coord]
    else:
        raise ValueError("Joueur non valide.")

def emplacement_case_libre(coord):
    x,y = coord
    return case_plateau[(x,y)]
    

def supprime_unite(nom):
    unite_supp = differentunite[nom]
    clna.Unite.list_Unite.remove(unite_supp)
    del differentunite[nom]
    if unite_supp.joueur == 1:
        clna.Unite.list_Unite_joueur1.remove(unite_supp)
    else:
        clna.Unite.list_Unite_joueur2.remove(unite_supp)
def check_porte(unite,cible):
    x1,y1 = unite.coord
    x2,y2 = cible.coord
    return unite.portee >= int(((x1-x2)**2+(y1-y2)**2)**(1/2))
    
def attaquer(unite, cible):
    print(unite.coord,cible.coord)
    #regarde la portée
    x1,y1 = unite.coord
    x2,y2 = cible.coord
    if check_porte(unite, cible):
        cible.pv -= unite.degats
        if cible.pv < 0:
            print(f"Attaque réussie ! l'{cible.nom} est morte ")
            del cible
        else :
            print(f"Attaque réussie ! Points de vie restants de la cible : {cible.pv}")
    else:
        print("La cible est hors de portée")
def attaqueVille(unite):
    if unite.joueur == 1:
        if check_porte(unite, clna.Paris):
            clna.Paris.PV -= unite.degats
        
    if unite.joueur == -1:
        if check_porte(unite, clna.Lille):
            clna.Lille.PV -= unite.degats
        
        
    else:
        raise "Erreur de joueur"
def bouge(unite,direction):
    x,y = unite.coord
    if unite.pm < 1 : #check cout en déplacement
        return "déplacement impossible"
    
    if direction == "haut":
        if y-1>=0 and emplacement_case_libre((x,y-1)):             
            unite.coord = (x,y-1)
        else:
            return "déplacement impossible"
        
    if direction == "bas":
        if y+1<=9 and emplacement_case_libre((x,y+1)):
            unite.coord = (x,y+1)        
        else:
            return "déplacement impossible"
        
    if direction == "droite":
        if x+1<=9 and emplacement_case_libre((x+1,y)):
            unite.coord = (x+1,y)
        else:
            return "déplacement impossible"
    if direction == "gauche":
        if x-1>=0 and emplacement_case_libre((x-1,y)):
            unite.coord = (x-1,y)
        else:
            return "déplacement impossible"
def check_etat():
    for unite in clna.Unite.list_Unite:
        if unite.pv < 0:
            supprime_unite(unite.nom)