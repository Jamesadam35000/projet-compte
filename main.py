from Compte import *
import random

user = 'Toto'
SOLDEE = random.randint(500, 10000)
SOLDEC = random.randint(0, 1000)
NUMCOMPTEE = random.randint(1000000000, 9999999999)
NUMCOMPTECOURANT = random.randint(1000000000, 9999999999)
AUTORISATIONDECOUVERT = random.randint(0, 1000)
INTERET = round(random.random(), 2)
AGIOS = round(random.random(), 2)

compteE = CompteEpargne(INTERET, SOLDEE, NUMCOMPTEE, user)
compteC = CompteCourant(AUTORISATIONDECOUVERT, AGIOS, SOLDEC, NUMCOMPTECOURANT, user)


def session():
    """implentez la fonction"""
    variable_sortie = True
    while variable_sortie:
        print(user + """, que voulez vous faire ?
        
                1 - Opération 
                2 - Afficher solde
                3 - Quitter""")
        choix = input()

        if choix == "1":
            print("opé")
        elif choix == "2":
            print("solde")
        elif choix == "3":
            variable_sortie = False
        else:
            print("Saisie invalide, veuillez recommencer s'il vous plait !")


if __name__ == '__main__':
    session()
