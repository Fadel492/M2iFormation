
import sys
import numpy as np
import Point as P
import Agenda as A
import Compte as C

pt1 = P.Point(0, 2)
pt2 = P.Point(1, 3)
print(
    f"Creation du premier point A1 d'abcisse {pt1._x} et d'ordonnée {pt2._y}")
print(
    f"Creation du premier point B1 d'abcisse {pt2._x} et d'ordonnée {pt2._y}")
d = P.Point.distance(pt1, pt2)
M = P.Point.milieu(pt1, pt2)
print(
    f"La distance entre le point A et B de coordonnée respectives A({pt1._x} , {pt2._y}) et  B({pt2._x} , {pt2._y}) est {d}cm")
print(
    f"Le milieu entre le point A et B de coordonnée respectives A({pt1._x} , {pt2._y}) et B({pt2._x} , {pt2._y}) est {M}")
print("*************************** Fin du programme ***************************************************************")
print("Lancement du programme2...")
C1 = C.Compte(123, "DIAKHATE", 100, 3)
print(
    f"Les information de votre compte est nom: {C1.nom_client}, le solde:{C1.solde} euro et numero de compte:{C1.num_comp}")
versement = C1.versement(100, 123)
print(f"Votre nouvau solde est de {versement} euro")
print("****************************************************************************")
retrait = C1.retrait(50)
print("****************************************************************************")
virement = C1.virement(124, 100)

print("*************** Fin programme ******************************")

mon_agenda = A.Agenda("fadel", "DIAKHATE", "0695458141",
                      "f.diakhate@outlook.fr", "15 rue Genin 93200")
mon_agenda.ajouContact("Ibrahima", "SARR", "07871245",
                       "ibra12@gmail.com", "22 rue clement 95100")
# .
# mon_agenda.modifier_contact()
# mon_agenda.tri_contact()
# mon_agenda.suprimer_contact()
