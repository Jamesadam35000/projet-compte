from Compte import Compte

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

