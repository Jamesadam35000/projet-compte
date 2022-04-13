from Compte import Compte
from Compte import CompteCourant
from Compte import CompteEpargne

# test de mon affichage du solde de ma classe compte

# compte = Compte(60, 14515161, "James")
# # compte.afficherSolde()
# #
# # # Test de la méthode retrait de ma classe compte
# #
# compte.retrait(-52)
# compte.afficherSolde()
#
#
# # Test de la methode versement de ma classe compte
#
# compte.versement(256)
# compte.afficherSolde()
# compte.versement(-256)
# compte.afficherSolde()
#
# Test de ma classe CompteCourant

CompteCourant = CompteCourant(100,0.1,100,14514521,"James")
CompteCourant.retrait(110)
CompteCourant.afficherSolde()

# # Test de ma classe CompteEpargne
#
CompteEpargne = CompteEpargne(0.1,1000,14515161,"James")
CompteEpargne.afficherSolde()
CompteEpargne.versement(100)
CompteEpargne.appliquerInteret()
CompteEpargne.afficherSolde()

