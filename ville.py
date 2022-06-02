from constantes import Constantes

class Ville:

    def __init__(self, position, relation, couleur, name, centre = False):
        """
        créé une ville

        exemple for Alger:

        Alger = (
        position = (280, 167)
        centre = False
        infection = {Constantes.RED    : 0,
                     Constantes.BLUE   : 0,
                     Constantes.BLACK  : 0,
                     Constantes.YELLOW : 0
                     }
        relation = (Constantes.MADRID, Constantes.PARIS, Constantes.ISTANBUL, Constantes.LE_CAIRE)

        couleur =  Constantes.BLACK
        name = Constantes.ALGER
        )

        :param position:
        :param centre:
        :param infection:
        :param relation:
        :param couleur:
        :param name:
        """
        self.POSITION = position
        self.centre = centre
        self.infection = {Constantes().RED    : 0,
                     Constantes().BLUE   : 0,
                     Constantes().BLACK  : 0,
                     Constantes().YELLOW : 0
                     }
        self.RELATION = relation
        self.COULEUR = couleur
        self.NAME = name

