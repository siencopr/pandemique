
class Ville:

    def __init__(self, constantes, position, relation, couleur, name):

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
        self.Constantes = constantes
        self.POSITION = position
        self.centre_recherche = False
        self.infection = {self.Constantes.RED    : 0,
                          self.Constantes.BLUE   : 0,
                          self.Constantes.BLACK  : 0,
                          self.Constantes.YELLOW : 0
                          }
        self.RELATION = relation
        self.COULEUR = couleur
        self.NAME = name
        self.can_explose = True

    def se_faire_infecter(self, couleur):
        print("la ville", self.NAME, "a été infectée par le virus", end = " ")


        if self.infection[couleur] < 3:
            self.infection[couleur] += 1
            print(":", self.infection)
        elif self.can_explose:
            print("\n la ville", self.NAME, "a déjà été infectée 3 fois... \n nous assistons donc a une \U00002623 ECLOSION \U00002623")
            self.can_explose = False
            for name_ville in self.RELATION:
                self.Constantes.dico_ville[name_ville].se_faire_infecter(couleur)



