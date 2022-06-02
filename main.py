#import
from constantes import Constantes
from ville import Ville
from joueur import Joueur
from jeu import Jeu

#variable

Constantes = Constantes()
Jeu = Jeu()

#ville
dico_ville = {
    #ville Bleu
    Constantes.SAN_FRANCISCO     : Ville(position = ( 32, 139), relation = (Constantes.TOKYO, Constantes.MANILLE, Constantes.LOS_ANGELES, Constantes.CHICAGO),                             couleur = Constantes.BLUE, name = Constantes.SAN_FRANCISCO),
    Constantes.PARIS             : Ville(position = (272, 122), relation = (Constantes.MADRID, Constantes.LONDRES, Constantes.ESSEN, Constantes.MILAN, Constantes.ALGER),                  couleur = Constantes.BLUE, name = Constantes.PARIS),
    Constantes.CHICAGO           : Ville(position = ( 85, 122), relation = (Constantes.SAN_FRANCISCO, Constantes.LOS_ANGELES, Constantes.MEXICO, Constantes.ATLANTA, Constantes.MONTREAL), couleur = Constantes.BLUE, name = Constantes.CHICAGO),
    Constantes.MONTREAL          : Ville(position = ( 32, 139), relation = (Constantes.WASHINGTON, Constantes.NEW_YORK, Constantes.CHICAGO),                                               couleur = Constantes.BLUE, name = Constantes.MONTREAL),
    Constantes.NEW_YORK          : Ville(position = (160, 124), relation = (Constantes.MONTREAL, Constantes.WASHINGTON, Constantes.MADRID, Constantes.LONDRES),                            couleur = Constantes.BLUE, name = Constantes.NEW_YORK),
    Constantes.LONDRES           : Ville(position = (100, 240), relation = (Constantes.ESSEN, Constantes.PARIS, Constantes.MADRID, Constantes.NEW_YORK),                                   couleur = Constantes.BLUE, name = Constantes.LONDRES),
    Constantes.ATLANTA           : Ville(position = (113, 153), relation = (Constantes.CHICAGO, Constantes.MIAMI, Constantes.WASHINGTON),                                                  couleur = Constantes.BLUE, name = Constantes.ATLANTA, centre = True),
    Constantes.WASHINGTON        : Ville(position = (147, 153), relation = (Constantes.ATLANTA, Constantes.MONTREAL, Constantes.NEW_YORK, Constantes.MIAMI),                               couleur = Constantes.BLUE, name = Constantes.WASHINGTON),
    Constantes.MADRID            : Ville(position = (232, 143), relation = (Constantes.SAO_PAULO, Constantes.NEW_YORK, Constantes.LONDRES, Constantes.PARIS, Constantes.ALGER),            couleur = Constantes.BLUE, name = Constantes.MADRID),
    Constantes.ESSEN             : Ville(position = (281,  85), relation = (Constantes.SAINT_PETERSBOURG, Constantes.MILAN, Constantes.PARIS, Constantes.LONDRES),                         couleur = Constantes.BLUE, name = Constantes.ESSEN),
    Constantes.MILAN             : Ville(position = (299, 105), relation = (Constantes.ISTANBUL, Constantes.PARIS, Constantes.ESSEN),                                                      couleur = Constantes.BLUE, name = Constantes.MILAN),
    Constantes.SAINT_PETERSBOURG : Ville(position = (329,  85), relation = (Constantes.MOSCOU, Constantes.ISTANBUL, Constantes.ESSEN),                                                     couleur = Constantes.BLUE, name = Constantes.SAINT_PETERSBOURG),

    #ville Noir
    Constantes.ALGER : Ville(position = (280, 167), relation = (Constantes.MADRID, Constantes.PARIS, Constantes.ISTANBUL, Constantes.LE_CAIRE), couleur = Constantes.BLACK, name = Constantes.ALGER),

}

#joueur

joueur_1 = Joueur(position= dico_ville[Constantes.ALGER], pouvoir= False, inventaire= [])

#fonction

for a in range(5):
    print("*"*15, "\n"*2, "\n**** pioche ****" )

    for i in range(2):
        carte_joueur = Jeu.pioche_d_une_carte_joueur(Constantes.Tas_de_carte_joueur)
        joueur_1.inventaire.append(carte_joueur)
        print("vous avez piochez la carte", carte_joueur)

    print("*" * 16, "\n" * 2, "\n**** action ****")

    for i in range(4): #les 4 actions
        print("vous êtes actuelement a", joueur_1.position.NAME)
        print("vous pouvez faire les action suivante : \n",Jeu.action_possible(joueur_1))

        action = input("quel action voulez vous faire ?")

        if action == Constantes.VOITURE:
            print("vous pouvez allez sur les villes :", Jeu.deplacement(joueur_1))
            direction = input("ou voulez vous allez ?")
            joueur_1.position = dico_ville[direction]

        if action == Constantes.DESINFECTION_BLUE:
            joueur_1.position.infection[Constantes.BLUE] -= 1

            print("la ville", joueur_1.position.NAME, "a été desinfecter du virus bleu")
            print(joueur_1.position.NAME, joueur_1.position.infection)

    print("*" * 15, "\n" * 2, "** infections **")

    for i in range(2):
        ville_propagation_name = Jeu.pioche_de_la_ville_infecter(Constantes.Tas_de_carte_propagation)
        ville_propagation = dico_ville[ville_propagation_name]
        ville_propagation.infection[ville_propagation.COULEUR] += 1

        print("la ville", ville_propagation.NAME, "a été infectée par le virus")

        print(ville_propagation.infection)

#codde principale
