from Compte import Compte

class CompteEpargne(Compte):

    """Classe qui nous permettra pour un compte epargne de lui
        donner un pourcentage d'interet et d'appliquer ces interets
        à ce compte"""

    def __init__(self, pourcentage_interet:float):
        self.pourcentage_interet = pourcentage_interet

    def appliquerInteret(self):
        """"""
        self._solde *= self.pourcentage_interet
        return self._solde