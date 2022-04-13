from abc import ABC

""" Création de mon module Compte"""

class Compte(ABC):
    """ Implementation de la classe compte, elle
    nous permettra de faire des retraits, versements
     et afficher le solde pour un comtpe donné """

    def __init__(self, solde: float, numero_compte: int, nom_proprietaire: str):
        self._solde = solde
        self.__numero_compte = numero_compte
        self.nom_proprietaire = nom_proprietaire

    def retrait(self, montant_retrait : float=0):
        """Méthode qui permet de retirer le montant que
        l'utilisateur souhaite pour un compte donné. Ici,
        il ne peut pas utiliser le signe - avec l'interface"""

        if self._solde >= montant_retrait:
            self._solde += montant_retrait
        else:
            raise Exception("Opération invalide, vous n'avez pas assez d'argent")

    def versement(self, montant_versement: float=0):
        """Méthode qui permet d'ajouter le montant que
        l'utilisateur souhaite pour un compte donné. Ici,
        il peut utiliser un signe "-" avec l'interface"""
        self._solde += montant_versement

    def afficherSolde(self):
        """Affichage du solde pour un compte"""
        return str(round(self._solde,2))+"€"


class CompteCourant(Compte):
    """Classe qui nous permettra pour un compte courrant de lui
    donner une autorisation de découvert, un pourcentage d'agios
    et d'appliquer des agios à ce compte"""

    def __init__(self, autorisation_decouvert: float, pourcentage_agios: float, solde: float, numero_compte: int,
                 nom_proprietaire: str):
        super().__init__(solde, numero_compte, nom_proprietaire)
        self.autorisation_decouvert = autorisation_decouvert
        self.pourcentage_agios = pourcentage_agios

    def appliquerAgios(self):
        """"""
        if self._solde < 0:
            self._solde *= (1 + self.pourcentage_agios)

    def retrait(self, montant_retrait: float = 0):
        if (self._solde + montant_retrait) > -1 * self.autorisation_decouvert:
            self._solde += montant_retrait
            self.appliquerAgios()
        elif (self._solde + montant_retrait) < -1 * self.autorisation_decouvert:
            raise Exception ("Opération invalide vous allez dépasser le seuil de découvert autorisé ")

    def versement(self, montant_versement=0):
        Compte.versement(self, montant_versement)
        self.appliquerAgios()
        return self._solde


class CompteEpargne(Compte):
    """Classe nous permettra pour un compte epargne de lui
        donner un pourcentage d'interet et d'appliquer ces
        interets à ce compte. Un compte epargne ne peut pas
        aller en dessous de 20€, pour les retraits on applique
        donc aucuns agios."""

    def __init__(self, pourcentage_interet: float, solde: float, numero_compte: int, nom_proprietaire: str):
        super().__init__(solde, numero_compte, nom_proprietaire)
        self.pourcentage_interet = pourcentage_interet

    def appliquerInteret(self):
        """decrire cette methode"""
        if self._solde > 0:
            self._solde *= (1 + self.pourcentage_interet)

    def retrait(self, montant_retrait: float = 0):
        if self._solde + montant_retrait < 20:
            raise Exception ("Impossible d'aller en dessous de 20€ pour un compte epargne")
        Compte.retrait(self, montant_retrait)
        self.appliquerInteret()

    def versement(self, montant_versement : float=0):
        Compte.versement(self, montant_versement)
        self.appliquerInteret()
