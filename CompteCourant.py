import Compte

class CompteCourant(Compte):

    """Classe qui nous permettra pour un compte courrant de lui
    donner une autorisation de découvert, un pourcentage d'agios
    et d'appliquer des agios à ce compte"""

    def __init__(self, autorisation_decouvert:float, pourcentage_agios:float):
        self.autorisation_decouvert = autorisation_decouvert
        self.pourcentage_agios = pourcentage_agios

    def appliquerAgios(self):
        """"""
        self._solde *= (1-self.pourcentage_agios)
        return self._solde