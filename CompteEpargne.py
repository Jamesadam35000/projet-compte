import Compte

class CompteEpargne(Compte):

    """Classe qui nous permettra pour un compte epargne de lui
        un pourcentage d'interet et d'appliquer ces interets à
        ce compte"""

    def __init__(self, pourcentageInteret:float):
        self.pourcentage_interet = pourcentageInteret

    def appliquerInteret(self):
        """ """