# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Classe

class Compte:
    """ documenter ma classe"""
    def __init__(self, solde:float, numeroCompte:int, nomProprietaire:str ):
        self._solde = solde
        self.__numero_compte = numeroCompte
        self.nom_proprietaire = nomProprietaire

    def retrait(self, montant_retrait):
        """"""
        self._solde -= montant_retrait

    def versement(self, montant_versement):
        """"""
        self._solde += montant_versement

    def afficherSolde(self):
        """"""
        print(self._solde)

class CompteCourant(Compte):
    def __init__(self, autorisationDecouvert:float, pourcentageAgios:float):
        self.autorisation_decouvert = autorisationDecouvert
        self.pourcentage_agios = pourcentageAgios

    def appliquerAgios(self):
        """"""


class CompteEpargne(Compte):
    """documenter ma classe"""
    def __init__(self, pourcentageInteret:float):
        self.pourcentage_interet = pourcentageInteret

    def appliquerInteret(self):
        """ """


# Fonction


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input("Bienvenu sur vos comptes, choisissez-en un (courant ou epargne) :")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
