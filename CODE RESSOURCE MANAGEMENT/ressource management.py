'''
ville dans laquelle on peut installer des batiments 
les villes produisent des ressources : 
    -de la production : prod
    -de l'or : or
    -de la science : sc
    -nourriture : no
    autre argument pris en compte 
-force armé
les villes accumulent une reserve de production auxquel s'ajoute la production de la ville à chaque tour que le joueur peut utiliser sous la forme d'un coût fixe de prod
pareille pour la science et l'oril y a une réserve qui s'accumule
-nombre de territoire disponible par défaut 20
La production permet de construire toutes les construction, merveilles et unités 
l'or permet d'acheter des batiments et des unités 
la science permet de dévellopper des technologie pour augmenter le rendement des batiments 
Ajout d'un nouvel atribut, le nombre d'habitant, 2 nourriture = 1 habitant, chaque habitant peut produire une des trois ressources exprimé précedemment : or,prod,sc
liste des batîments: ont besoin d'un territoire libre et supprime un territoire libre
ferme ajoute +2 de nourriture un coût fixe de 10 au début et augmente de 5 à chaque ferme construite
usine ajoute +2 prod un coût fixe de de 10 au début et augmente de 5 à chaque usine construite
marché ajoute +2 or un coût fixe de de 10 au début et augmente de 5 à chaque marché construite
université ajoute +2 sc un coût fixe de de 10 au début et augmente de 5 à chaque université construite
caserne permet de former des unités -> une unité coûte 10 de production et ajoute +1 à la force armé 
Technologie:
construction : permet de construire des usines coute 20 de science de la reserve 
armement : ajoute +2 à la force armé au lieu de +1 coute 20 de science de la reserve
potterie : ajoute +2 de prod à chaque usine coute 30 de science de la reserve
écriture : permet de construire les universités coute 20 de science de la reserve
éducation : ajoute +2 de science à chaque université coute 20 de science de la reserve
monnaie : permet la construction des marchés coute 20 de science de la reserve
banque : ajoute +2 d'or à tous les marchés coute 30 de science de la reserve
Merveilles, les merveilles ne peuvent être construit qu'une fois, ont besoin d'un territoire libre et supprime un territoire libre
Alhambra : ajoute +50% à la force armé -> coûte un coût fixe de 50 prod
Amundsen : multiplie par 20% la science produite et de 10% la production -> coûte un coût fixe de 100  prod
Casa de Contratación : +15% production, +15% or -> coûte un coût fixe de 75 prod
Great Bath : ajoute 1 de production pour chaque habitant  -> coûte un coût fixe de 100 prod
Huey Teocalli : +50% production nourriture -> coûte un coût fixe de 150 prod
'''