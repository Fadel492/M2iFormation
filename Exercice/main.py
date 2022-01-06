#from _typeshed import Self
import sys
import numpy as np

""" 
Ecrire une classe qui permet de représenter un point dans un plan (abscisse, ordonnée)
- Ecrire le constructeur
- Ecrire les getters / setters
- Ecrire la représentation graphique sous la forme « (abscisse, ordonnée) »
- Rédefinir l’opérateur d’addition de deux points, qui permet de créer un nouveau point dont les coordonnées sont la somme des coordonnées des 2 points additionnés
- Ecrire la méthode distance qui prend en paramètre un point et renvoie la distance dans le plan avec le point appelant
o Distance = racine de ((x1-x2)²+(y1-y2)²)
- Ecrire les méthodes qui permettent de savoir si un point est plus grand, plus petit ou égal à un autre (pour > et < on prendra la distance au point d’origine)
- Ecrire la méthode milieu qui prend en paramètre un point et renvoie un objet point se trouvant au milieu du segment formé par le point appelant et le point en paramètre
o Milieu ➔ x=(x1+x2)/2 , y=(y1+y2)/2

"""


class point:


    def __init__(self,abcisse,ordonne):
        #print("creation d'un point.......")
        self._X=abcisse
        self._Y=ordonne

    def _getabcisse(self):
        return self._X

    def _setabcisse(self,newAbcisse):
         self._X=newAbcisse

    def _getordonne(self):
        return self._Y    

    def _setordonne(self,newordonne):
        self._Y=newordonne

    def AdditionPoint(A,B):

        absf=A._X - B._X
        ordf=A._Y - B._Y
        return point(absf,ordf)


        

    def distance(P1,P2):
        resultat=np.sqrt((P2._X - P1._Y)**2+(P2._Y - P1._X)**2)
        return resultat

    def Milieu(P1,P2):
        return ((P1._X + P2._X)/2,(P1._Y + P2._Y)/2)
        

print("Lancement du programme1...")

A1=point(0,2)
B1=point(1,3)

print(f"Creation du premier point A1 d'abcisse {A1._X} et d'ordonnée {A1._Y}")
print("****************************************************************************")
print(f"Creation du premier point B1 d'abcisse {B1._X} et d'ordonnée {B1._Y}")

d=point.distance(A1,B1)

M=point.Milieu(A1,B1)
print("****************************************************************************")
print(f"La distance entre le point A et B de coordonnée respectives A({A1._X} , {A1._Y}) et  B({B1._X} , {B1._Y}) est {d}cm")
print("****************************************************************************")
print(f"Le milieu entre le point A et B de coordonnée respectives A({A1._X} , {A1._Y}) et B({B1._X} , {B1._Y}) est {M}")

print("*************************** Fin du programme ***************************************************************")

""" 
Ecrire une classe compte bancaire qui a pour attribut un numero de compte, un nom de client, le solde, 
le nombre d’opérations réalisées et une variable de classe nb max d’opérations
- Ecrire le constructeur du compte
- Ecrire les getters
- Ecrire la représentation graphique sous la forme « nom : xxx, numCpte : yyy, solde : 100, nbreOp : 3 »
- Ecrire une méthode versement qui gère les versements
- Ecrire une méthode retrait qui gère les retraits (notamment s’assure que le compte est suffisamment provisionné)
- Ecrire une méthode virement qui permet d’envoyer de l’argent en renseignant le numéro de compte de destination
- Ecrire une méthode frais qui applique des frais à hauteur de 1% de l’opération pour chaque opération 
  en plus du nb max d’opérations par compte ➔ Les frais s’appliquent à tous type d’opération hormis l’affichage du compte
"""

class CompteBancaire:
    NbmaxOp=0

    def __init__(self,Numcomp,Nomclient,solde,Nboprealise):

        self._Numcomp=Numcomp
        self._Nomclient=Nomclient
        self._solde=solde
        self._Nboprealise=Nboprealise
    
    def _getNumcomp(self):
        return self._Numcomp

    def _getNomclien(self):
        return self._Nomclient

    def _getsolde(self):
        return self._solde

    def _getNboprealise(self):
        return self._Nboprealise
        

    def Versement(self,soldeVersement,idVersement):

        print(f"Versement de {soldeVersement} euro en cours sur ce compte compte ...")
        if(self._Numcomp==idVersement):
            self._solde=self._solde+soldeVersement
        else:
            print("le numero de compte saisie est invalide")
        return self._solde

    def Retrait(self,soldeRetrait):
        if(self._solde <=soldeRetrait):
            print("La somme que vous voulais retiré est superieur à votre solde")
            print("Veuillez choisir un montant plus petite")
        else:
            print(f"vous avez retire {soldeRetrait} et il vous reste {self._solde-soldeRetrait} dans votre compte")
        
    def Virement(self,idvirement,soldeVirement):
        print(f"Virement de {soldeVirement} euro sur IBAN {idvirement} ...")



print("Lancement du programme2...") 
print("****************************************************************************")  
Compte_Fadel=CompteBancaire(123,"DIAKHATE",100,3)
print(f"Les information de votre compte est nom: {Compte_Fadel._Nomclient}, le solde:{Compte_Fadel._solde} euro et numero de compte:{Compte_Fadel._Numcomp}")

print("****************************************************************************")
Opversement=Compte_Fadel.Versement(100,123)
print(f"Votre nouvau solde est de {Opversement} euro")
print("****************************************************************************")
Opretrait=Compte_Fadel.Retrait(50)
print("****************************************************************************")
opVirement=Compte_Fadel.Virement(124,100)
