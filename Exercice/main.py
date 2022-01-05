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
        print("creation d'un point.......")
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


print("Lancement du programme...")

A1=point(0,2)
print(f"Creation du premier point d'abcisse {A1._X} et d'ordonnée {A1._Y}")
