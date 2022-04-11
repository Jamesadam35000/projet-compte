class Compte:

    """ Implementation de la classe compte, elle
    nous permettra de faire des retraits, versements
     et afficher le solde pour un comtpe donné """

    def __init__(self, solde: float, numero_compte: int, nom_proprietaire: str):
        self._solde = solde
        self.__numero_compte = numero_compte
        self.nom_proprietaire = nom_proprietaire

    def retrait(self, montant_retrait: int):

        """Méthode qui permet de retirer le montant que
        l'utilisateur souhaite pour un compte donné"""

        self._solde -= abs(montant_retrait)
        return self._solde

    def versement(self, montant_versement):

        """Méthode qui permet d'ajouter le montant que
        l'utilisateur souhaite pour un compte donné"""

        self._solde += montant_versement
        return self._solde

    def __repr__(self):

        """Affichage du solde pour un compte"""

        return self._solde