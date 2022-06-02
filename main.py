#import
from constantes import Constantes
from ville import Ville
from joueur import Joueur
from jeu import Jeu

#variable

Constantes = Constantes()
Jeu = Jeu()

#joueur

joueur_1 = Joueur(position= Constantes.dico_ville[Constantes.ALGER], pouvoir= False, inventaire= [])

#fonction
def pioche_n_carte_propagation(n):
    """
    simule la pioche de n carte propagation

    :param n:
    :return:
    """
    print("*" * 15, "\n" * 2, "** infections **")
    for i in range(n):
        ville_infecter = Jeu.pioche_de_la_ville_infecter()
        ville_infecter.se_faire_infecter(ville_infecter.COULEUR)

        print("la ville", ville_infecter.NAME, "a été infectée par le virus")

        print(ville_infecter.infection)


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


for a in range(5):
    pioche_n_carte_propagation(2)

    pioche_n_carte_joueur(2, joueur_1)

    print("*" * 16, "\n" * 2, "\n**** action ****")

    for i in range(4): #les 4 actions
        print("vous êtes actuelement a", joueur_1.position.NAME)
        print("vous pouvez faire les action suivante : \n",Jeu.action_possible(joueur_1))

        action = input("quel action voulez vous faire ?")

        if action == Constantes.VOITURE:
            print("vous pouvez allez sur les villes :", Jeu.deplacement(joueur_1))
            direction = input("ou voulez vous allez ?")
            joueur_1.position = Constantes.dico_ville[direction]

        if action == Constantes.DESINFECTION_BLUE:
            joueur_1.position.infection[Constantes.BLUE] -= 1

            print("la ville", joueur_1.position.NAME, "a été desinfecter du virus bleu")
            print(joueur_1.position.NAME, joueur_1.position.infection)



    pioche_n_carte_propagation(2)



#codde principale
