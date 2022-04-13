from Compte import *
import random

"""Constante pour les choix"""

COMPTE_COURANT = "1"
COMPTE_EPARGNE = "2"

def ui_saisie_montant():
    """
    Cette fonction permet à l'utilisateur de choisir le montant de
    son virement pour un de ses comptes qu'il choisit auparevent
    """
    global montant
    choix_compte = None
    while choix_compte not in [COMPTE_COURANT, COMPTE_EPARGNE]:
        print(""" Sur quel compte ? 
        
                1 - Compte Courant
                2 - Compte Epargne
                 """)
        choix_compte = input()
    compte = compteC if choix_compte == COMPTE_COURANT else compteE
    print("Votre solde est de : " + compte.afficherSolde())
    print("Quel montant ?")
    try:
        montant = float(input())
    except ValueError:
        print("Vous vous êtes trompé, réecrivez un nombre décimale valable!")
        montant = 0
    compte.versement(montant) if montant > 0 else compte.retrait(montant)
    print("Votre solde est maintenant de : " + compte.afficherSolde()+"\n")


def ui_affichage_soldes():
    """
    Cette fonction permet à l'utilisateur l'affichage des soldes
    de ses comptes
    """
    print("Affichage des soldes : \n")
    print("Compte courant : " + compteC.afficherSolde())
    print("Compte Epargne : " + compteE.afficherSolde())
    print("\n")


def ui():
    """
    Cette fonction permet à l'utilisateur de chosir une des 3 options réalisable :
    opération, affichage des soldes ou quitter l'application.
    """

    variable_sortie = True
    while variable_sortie:
        print(user + """, que voulez vous faire ?
        
                1 - Opération 
                2 - Afficher solde
                3 - Quitter""")

        choix = input()

        match choix:
            case "1":
                ui_saisie_montant()
            case "2":
                ui_affichage_soldes()
            case "3":
                variable_sortie=False
            case _:
                print("Saisie invalide, veuillez recommencer s'il vous plait !")

user = 'Toto'
autorisation_decouvert = random.randint(0, 1000)
solde_compte_courant = random.randint(-autorisation_decouvert, 10000) #on met autorisation decouvert en valeur minimale pour ne pas se retrouver en dessous du seuil autorisé
solde_compte_epargne = random.randint(20, 10000)
num_compte_courant = random.randint(1000000000, 9999999999)
num_compte_epargne = random.randint(1000000000, 9999999999)
interet = 0.1 #round(random(),2)
agios = 0.1 #round(random(),2)

compteE = CompteEpargne(interet, solde_compte_epargne, num_compte_epargne, user)
compteC = CompteCourant(autorisation_decouvert, agios, solde_compte_courant, num_compte_courant, user)

if __name__ == '__main__':
    ui()
