from constantes import Constantes

class Jeu:
    def __init__(self):
        self.win = False
        self.Constantes = Constantes()


    def action_possible(self, joueur):

        liste_action_possible = [self.Constantes.VOITURE]

        if joueur.position.infection[self.Constantes.RED] > 0:
            liste_action_possible.append(self.Constantes.DESINFECTION_RED)
        if joueur.position.infection[self.Constantes.BLUE] > 0:
            liste_action_possible.append(self.Constantes.DESINFECTION_BLUE)
        if joueur.position.infection[self.Constantes.BLACK] > 0:
            liste_action_possible.append(self.Constantes.DESINFECTION_BLACK)
        if joueur.position.infection[self.Constantes.YELLOW] > 0:
            liste_action_possible.append(self.Constantes.DESINFECTION_YELLOW)

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

    def pioche_de_la_ville_infecter(self, liste_propagation):
        """
        simule la pioche d'une carte proagation

        :param n:
        :return:
        """
        nom = liste_propagation.pop(0)

        return nom




