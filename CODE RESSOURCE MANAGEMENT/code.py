class Ville:
    def __init__(self, nom, prod=0, or_=0, sc=0, no=0, force_armee=0, habitants=0, territoire_dispo=20):
        self.nom = nom
        self.prod = prod
        self.or_ = or_
        self.sc = sc
        self.no = no
        self.force_armee = force_armee
        self.habitants = habitants
        self.territoire_dispo = territoire_dispo
        self.reserve_prod = 0
        self.reserve_or = 0
        self.reserve_sc = 0

    def construire_batiment(self, batiment):
        cout_fixe_prod = 10
        cout_fixe_or = 10
        cout_fixe_sc = 10
        
        if batiment == "ferme":
            if self.territoire_dispo > 0:
                self.no += 2
                self.reserve_prod += cout_fixe_prod
                cout_fixe_prod += 5
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire une ferme.")
        elif batiment == "usine":
            if self.territoire_dispo > 0:
                self.prod += 2
                self.reserve_prod += cout_fixe_prod
                cout_fixe_prod += 5
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire une usine.")
        elif batiment == "marché":
            if self.territoire_dispo > 0:
                self.or_ += 2
                self.reserve_or += cout_fixe_or
                cout_fixe_or += 5
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire un marché.")
        elif batiment == "université":
            if self.territoire_dispo > 0:
                self.sc += 2
                self.reserve_sc += cout_fixe_sc
                cout_fixe_sc += 5
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire une université.")
        elif batiment == "caserne":
            if self.reserve_prod >= 10:
                self.force_armee += 1
                self.reserve_prod -= 10
            else:
                print("Pas assez de production en réserve pour former une unité.")

    def developper_technologie(self, technologie):
        if technologie == "construction":
            if self.reserve_sc >= 20:
                self.prod += 2  # Effet de la technologie
                self.reserve_sc -= 20
            else:
                print("Pas assez de science en réserve pour développer la technologie de construction.")
        elif technologie == "armement":
            if self.reserve_sc >= 20:
                self.force_armee += 2  # Effet de la technologie
                self.reserve_sc -= 20
            else:
                print("Pas assez de science en réserve pour développer la technologie d'armement.")
        elif technologie == "potterie":
            if self.reserve_sc >= 30:
                self.prod += 2  # Effet de la technologie
                self.reserve_sc -= 30
            else:
                print("Pas assez de science en réserve pour développer la technologie de potterie.")
        elif technologie == "écriture":
            if self.reserve_sc >= 20:
                self.sc += 2  # Effet de la technologie
                self.reserve_sc -= 20
            else:
                print("Pas assez de science en réserve pour développer la technologie d'écriture.")
        elif technologie == "éducation":
            if self.reserve_sc >= 20:
                self.sc += 2  # Effet de la technologie
                self.reserve_sc -= 20
            else:
                print("Pas assez de science en réserve pour développer la technologie d'éducation.")
        elif technologie == "monnaie":
            if self.reserve_sc >= 20:
                self.or_ += 2  # Effet de la technologie
                self.reserve_sc -= 20
            else:
                print("Pas assez de science en réserve pour développer la technologie de monnaie.")
        elif technologie == "banque":
            if self.reserve_sc >= 30:
                self.or_ += 2  # Effet de la technologie
                self.reserve_sc -= 30
            else:
                print("Pas assez de science en réserve pour développer la technologie de banque.")

    def construire_merveille(self, merveille):
        cout_fixe_prod = 0

        
        if merveille == "Alhambra":
            cout_fixe_prod = 50
            if self.territoire_dispo > 0:
                self.force_armee *= 1.5
                self.reserve_prod -= cout_fixe_prod
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire Alhambra.")
        elif merveille == "Amundsen":
            cout_fixe_prod = 100
            if self.territoire_dispo > 0:
                self.sc *= 1.2
                self.prod *= 1.1
                self.reserve_prod -= cout_fixe_prod
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire Amundsen.")
        elif merveille == "Casa de Contratación":
            cout_fixe_prod = 75
            if self.territoire_dispo > 0:
                self.prod *= 1.15
                self.or_ *= 1.15
                self.reserve_prod -= cout_fixe_prod
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire Casa de Contratación.")
        elif merveille == "Great Bath":
            cout_fixe_prod = 100
            if self.territoire_dispo > 0:
                self.prod += self.habitants
                self.reserve_prod -= cout_fixe_prod
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire Great Bath.")
        elif merveille == "Huey Teocalli":
            cout_fixe_prod = 150
            if self.territoire_dispo > 0:
                self.no *= 1.5
                self.reserve_prod -= cout_fixe_prod
                self.territoire_dispo -= 1
            else:
                print("Pas assez de territoire disponible pour construire Huey Teocalli.")
#code
def copier_ville(ville):
    # Créer une nouvelle instance de la classe Ville avec les mêmes attributs que la ville donnée en argument
    nouvelle_ville = Ville(ville.nom, ville.prod, ville.or_, ville.sc, ville.no, ville.force_armee, ville.habitants, ville.territoire_dispo)
    nouvelle_ville.reserve_prod = ville.reserve_prod
    nouvelle_ville.reserve_or = ville.reserve_or
    nouvelle_ville.reserve_sc = ville.reserve_sc
    nouvelle_ville.construction_dispo = ville.construction_dispo[:]
    nouvelle_ville.technologie_dispo = ville.technologie_dispo[:]
    nouvelle_ville.merveilles_construites = ville.merveilles_construites[:]
    
    return nouvelle_ville

def choisir_action_max_prod(ville):
    actions = ["construire_batiment", "developper_technologie", "construire_merveille"]
    liste_batiments = ["ferme", "usine", "marché", "université", "caserne"]
    liste_technologies = ["construction", "armement", "potterie", "écriture", "éducation", "monnaie", "banque"]
    liste_merveilles = ["Alhambra", "Amundsen", "Casa de Contratación", "Great Bath", "Huey Teocalli"]
    
    liste_elements_possibles = liste_batiments + liste_technologies + liste_merveilles
    
    valeur_max_prod = float('-inf')
    action_optimale = None
    
    for action in actions:
        for element in liste_elements_possibles:
            nouvelle_ville = copier_ville(ville)
            if action == "construire_batiment":
                nouvelle_ville.construire_batiment(element)
            elif action == "developper_technologie":
                nouvelle_ville.developper_technologie(element)
            elif action == "construire_merveille":
                nouvelle_ville.construire_merveille(element)
            
            valeur_prod_estimee = estimer_valeur_prod(nouvelle_ville)
            if valeur_prod_estimee > valeur_max_prod:
                valeur_max_prod = valeur_prod_estimee
                action_optimale = (action, element)
            
    return action_optimale, valeur_max_prod


# Exemple de fonction d'estimation de la valeur de la production après une action
def estimer_valeur_prod(ville):
    # Calculer la valeur de la production estimée après une action
    valeur_estimee = ville.prod
    return valeur_estimee

# Autres fonctions nécessaires (copier_ville, etc.)

# Exemple d'utilisation
ville_actuelle = Ville("Lille")
action_optimale = choisir_action_max_prod(ville_actuelle)
# Effectuer l'action optimale sur la ville
