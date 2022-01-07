import numpy as np


class Point:

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

    def __init__(self, abcisse, ordonne):
        #print("creation d'un point.......")
        self._x = abcisse
        self._y = ordonne

    def _getabcisse(self):
        return self._x

    def _setabcisse(self, abcisse):
        self._x = abcisse

    def _getordonne(self):
        return self._y

    def _setordonne(self, ordonne):
        self._y = ordonne

    def addition_point(pt1, pt2):
        """addition_point [summary]

        [extended_summary]

        Args:
            pt1 ([type]): [description]
            pt2 ([type]): [description]

        Returns:
            [type]: [description]
        """
        absf = pt1._x - pt2._x
        ordf = pt1._y - pt2._y
        pt = Point(absf, ordf)
        return pt

    def distance(pt1, pt2):
        a_carre = (pt1._x - pt1._y)**2
        b_carre = (pt2._y - pt1._x)**2
        resultat = np.sqrt(a_carre + b_carre)
        return resultat

    def calculer_milieu(pt1, pt2):
        """permet de calculer le milieu de deux points

        [extended_summary]

        Args:
            pt1 (Point): premiere extremite d'un segment
            pt2 (Point): deuxieme extremite du segment

        Returns:
           Point : ce point represente le milieu d'un segment
        """

        xm = (pt1._x + pt2._x)/2
        ym = (pt1._y + pt2._y)/2
        pt = Point(xm, ym)
        return pt
