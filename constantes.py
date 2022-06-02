
import random

class Constantes:

    def __init__(self):
        #couleur des infection
        self.RED = "red"
        self.BLUE = "blue"
        self.BLACK = "black"
        self.YELLOW = "yellow"

        #action
        self.VOITURE = "voiture"
        self.VOL_DIRECTE = "vol directe"
        self.VOL_CHARTER = "vol chatrer"
        self.DESINFECTION_RED = "desinfection red"
        self.DESINFECTION_BLUE = "desinfection blue"
        self.DESINFECTION_BLACK = "desinfection black"
        self.DESINFECTION_YELLOW = "desinfection yellow"


        #nom des villes
        #ville jaune
        self.LOS_ANGELES  = "Los angeles"
        self.MEXICO       = "Mexico"
        self.MIAMI        = "Miami"
        self.BOGOTA       = "Bogota"
        self.LIMA         = "Lima"
        self.SANTIAGO     = "Santiago"
        self.BUENOS_AIRES = "Buenos aires"
        self.SAO_PAULO    = "Sao paulo"
        self.LAGOS        = "Lagos"
        self.KHARTOUM     = "Kartoum"
        self.KINSHASA     = "Kinshasa"
        self.JOHANNESBURG = "Johannesburg"
        #ville bleu
        self.CHICAGO           = "Chicago"
        self.PARIS             = "Paris"
        self.MADRID            = "Madrid"
        self.SAN_FRANCISCO     = "San francisco"
        self.MONTREAL          = "Montreal"
        self.NEW_YORK          = "New york"
        self.ATLANTA           = "Atlanta"
        self.WASHINGTON        = "Washington"
        self.LONDRES           = "Londres"
        self.ESSEN             = "Essen"
        self.SAINT_PETERSBOURG = "Saint petersbourg"
        self.MILAN             = "Milan"
        #ville noir
        self.ISTANBUL = "istanbul"
        self.LE_CAIRE = "le caire"
        self.ALGER    = "alger"
        self.MOSCOU   = "moscou"
        self.BAGDAD   = "bagdad"
        self.RIYAD    = "riyad"
        self.KARACHI  = "karachi"
        self.TEHERAN  = "teheran"
        self.MUMBAI   = "mumbai"
        self.DELHI    = "delhi"
        self.CHENNAI  = "chennai"
        self.CALCUTA  = "calcuta"
        #ville rouge
        self.PEKIN             = "pekin"
        self.SEOUL             = "seoul"
        self.TOKYO             = "tokyo"
        self.SHANGAI           = "shangai"
        self.OSAKA             = "osaka"
        self.TAIPEI            = "taipei"
        self.HONG_KONG         = "hong kong"
        self.BANGKOK           = "bangkok"
        self.MANILLE           = "manille"
        self.HO_CHI_MINH_VILLE = "hô-chi-minh-ville"
        self.JAKARTA           = "jakarta"
        self.SYDNEY            = "sydney"

        """
        self.TAS_DE_CARTE_PROPAGATION = [self.PEKIN,
                                         self.SEOUL,
                                         self.TOKYO,
                                         self.SHANGAI,
                                         self.OSAKA,
                                         self.TAIPEI,
                                         self.HONG_KONG,
                                         self.BANGKOK,
                                         self.MANILLE,
                                         self.HO_CHI_MINH_VILLE,
                                         self.JAKARTA,
                                         self.SYDNEY,
                                         self.ISTANBUL,
                                         self.LE_CAIRE,
                                         self.ALGER,
                                         self.MOSCOU,
                                         self.BAGDAD,
                                         self.RIYAD,
                                         self.KARACHI,
                                         self.TEHERAN,
                                         self.MUMBAI,
                                         self.DELHI,
                                         self.CHENNAI,
                                         self.CALCUTA,
                                         self.CHICAGO,
                                         self.PARIS,
                                         self.MADRID,
                                         self.SAN_FRANCISCO,
                                         self.MONTREAL,
                                         self.NEW_YORK,
                                         self.ATLANTA,
                                         self.WASHINGTON,
                                         self.LONDRES,
                                         self.ESSEN,
                                         self.SAINT_PETERSBOURG,
                                         self.MILAN,
                                         self.LOS_ANGELES,
                                         self.MEXICO,
                                         self.MIAMI,
                                         self.BOGOTA,
                                         self.LIMA,
                                         self.SANTIAGO,
                                         self.BUENOS_AIRES,
                                         self.SAO_PAULO,
                                         self.LAGOS,
                                         self.KHARTOUM,
                                         self.KINSHASA,
                                         self.JOHANNESBURG]
        """

        self.Tas_de_carte_propagation = [self.CHICAGO,
                                         self.PARIS,
                                         self.MADRID,
                                         self.SAN_FRANCISCO,
                                         self.MONTREAL,
                                         self.NEW_YORK,
                                         self.ATLANTA,
                                         self.WASHINGTON,
                                         self.LONDRES,
                                         self.ESSEN,
                                         self.SAINT_PETERSBOURG,
                                         self.MILAN]

        self.Tas_de_carte_joueur = self.Tas_de_carte_propagation.copy() + ['carte spéciale une']

        random.shuffle(self.Tas_de_carte_propagation)
        random.shuffle(self.Tas_de_carte_joueur)

