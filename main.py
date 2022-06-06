#import
from constantes import Constantes
from joueur import Joueur
from jeu import Jeu

#variable
Constantes = Constantes()
Jeu = Jeu()
n_joueur = 1

#cree_les_joueur
joueur_1 = Joueur(position=Constantes.dico_ville[Constantes.ATLANTA], pouvoir=False, inventaire=[])
joueur_2 = Joueur(position=Constantes.dico_ville[Constantes.ATLANTA], pouvoir=False, inventaire=[])
if n_joueur >= 3:
    joueur_3 = Joueur(position=Constantes.dico_ville[Constantes.ATLANTA], pouvoir=False, inventaire=[])
if n_joueur >= 4:
    joueur_4 = Joueur(position=Constantes.dico_ville[Constantes.ATLANTA], pouvoir=False, inventaire=[])


#fonction
def pioche_de_la_ville_infecter():
    """
    simule la pioche d'une carte proagation

    :param n:
    :return:
    """
    nom = Constantes.Tas_de_carte_propagation.pop(0)
    ville = Constantes.dico_ville[nom]

    return ville


def pioche_n_carte_propagation(n):
    """
    simule la pioche de n carte propagation

    :param n:
    :return:
    """
    print("*" * 15, "\n" * 2, "** infections **")
    for i in range(n):
        ville_infecter = pioche_de_la_ville_infecter()
        ville_infecter.se_faire_infecter(ville_infecter.COULEUR)




def pioche_n_carte_joueur(n, joueur):
    """
    simule la pioche de n carte joueur par le joueur

    :param n:
    :param joueur:
    :return:
    """

    print("*" * 15, "\n" * 2, "\n**** pioche ****")

    for i in range(n):
        carte_joueur = Jeu.pioche_d_une_carte_joueur(Constantes.Tas_de_carte_joueur)
        joueur.inventaire.append(carte_joueur)
        print("vous avez piochez la carte", carte_joueur)


def infection_debut():
    for a in range(1,4):
        for i in range(3):
            ville = pioche_de_la_ville_infecter()
            ville.infection[ville.COULEUR] = a
            print("la ville", ville.NAME, "a été infectée par le virus :",ville.infection )


def initialisation():
    infection_debut()
    Constantes.dico_ville[Constantes.ATLANTA].centre_recherche = True  # atlanta comence avec un centre de recherche des le debut de la partie

    if n_joueur == 2:
        pioche_n_carte_joueur(4, joueur_1)
        pioche_n_carte_joueur(4, joueur_2)
    if n_joueur == 3:
        pioche_n_carte_joueur(3, joueur_1)
        pioche_n_carte_joueur(3, joueur_2)
        pioche_n_carte_joueur(3, joueur_3)
    if n_joueur == 4:
        pioche_n_carte_joueur(2, joueur_1)
        pioche_n_carte_joueur(2, joueur_2)
        pioche_n_carte_joueur(2, joueur_3)
        pioche_n_carte_joueur(2, joueur_4)





def tour_de_jeu_joueur(joueur):
    #pioche_n_carte_propagation(4)

    pioche_n_carte_joueur(2, joueur)

    print(joueur.inventaire)

    print("*" * 16, "\n" * 2, "\n**** action ****")

    for i in range(4):  # les 4 actions
        print("vous êtes actuelement a", joueur.position.NAME)
        print("vous pouvez faire les action suivante : \n", Jeu.action_possible(joueur))

        action = input("quel action voulez vous faire ?")

        if action not in Jeu.action_possible(joueur):
            print("triche, action non possible")

        if action == Constantes.VOITURE:
            print("vous pouvez allez sur les villes :", Jeu.deplacement(joueur))
            direction = input("ou voulez vous allez ?")
            joueur.position = Constantes.dico_ville[direction]

        if action == Constantes.DESINFECTION_BLUE:
            joueur.position.infection[Constantes.BLUE] -= 1

            print("la ville", joueur.position.NAME, "a été desinfecter du virus bleu")
            print(joueur.position.NAME, joueur.position.infection)

        if action == Constantes.VOL_CHARTER:
            print("vous pouvez aller dans les villes", Constantes.dico_ville.keys())

            ville = input("ou voulez vous allez")

            joueur.position = Constantes.dico_ville[ville]

        if action == Constantes.NAVETTE:
            ville_equipe_de_centre = []
            for ville_name in Constantes.dico_ville:
                if Constantes.dico_ville[ville_name].centre_recherche:
                    ville_equipe_de_centre.append(ville_name)
            print("vous pouvez utilisez la navette pour aller dans les villes", ville_equipe_de_centre)

            ville_arrive_name = input("ou voulez vous allez ?")

            joueur.position = Constantes.dico_ville[ville_arrive_name]

        if action == Constantes.CONSTRUIR_CENTRE:
            joueur.position.centre_recherche = True

    pioche_n_carte_propagation(2)
    
#code principale
infection_debut()

for a in range(5):
    tour_de_jeu_joueur(joueur_1)



