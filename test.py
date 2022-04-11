from Compte import Compte
from CompteCourant import CompteCourant

compte = Compte(8523, 14515161, "James")
compte.afficherSolde()

compte.retrait(256)
compte.afficherSolde()
compte.retrait(-256)
compte.afficherSolde()

compte.versement(256)
compte.afficherSolde()
compte.versement(-256)
compte.afficherSolde()

