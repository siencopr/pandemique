from constantes import Constantes

class Jeu:
    def __init__(self):
        self.win = False
        self.constantes = Constantes()


    def action_possible(self, joueur):

        liste_action_possible = [self.constantes.VOITURE]

        if joueur.position.infection[self.constantes.RED] > 0:
            liste_action_possible.append(self.constantes.DESINFECTION_RED)
        if joueur.position.infection[self.constantes.BLUE] > 0:
            liste_action_possible.append(self.constantes.DESINFECTION_BLUE)
        if joueur.position.infection[self.constantes.BLACK] > 0:
            liste_action_possible.append(self.constantes.DESINFECTION_BLACK)
        if joueur.position.infection[self.constantes.YELLOW] > 0:
            liste_action_possible.append(self.constantes.DESINFECTION_YELLOW)

        return liste_action_possible

    def deplacement(self, joueur):

        liste_ville_arrive_possible = joueur.position.RELATION

        return liste_ville_arrive_possible

    def pioche_d_une_carte_joueur(self, liste_carte_joueur):
        """

        :return:
        """

        nom = liste_carte_joueur.pop(0)

        return nom

    def pioche_de_la_ville_infecter(self):
        """
        simule la pioche d'une carte proagation

        :param n:
        :return:
        """
        nom = self.constantes.Tas_de_carte_propagation.pop(0)
        ville = self.constantes.dico_ville[nom]

        print(ville)

        return ville




