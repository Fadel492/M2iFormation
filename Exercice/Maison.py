class Maison:

    def __init__(self, nom):
        self.couleur_principal = ["Vert", "Jaune", "Rouge", "Bleu"]
        self.nom = nom
        # self.couleur_principal = couleur_principal


class Sort:
    def __init__(self, nom, couleur_sort, categorie, degats, vie):
        self.nom = nom
        self.couleur_sort = couleur_sort
        self.degats = degats
        self.vie = vie


class Personne:
    def __init__(self, nom, prenom, age, vie):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.vie = vie


class Sorciere(Personne):
    def __init__(self, maison1, object_sort, vie_initial=100):

        self.vie_initial=vie_initial
        self.maison = maison1
        self.object_sort = object_sort

    point_fort = ["Malediction", "Enchantement",
                  "Metamorphose", "Malefices"]
    point_faible = ["Malediction", "Enchantement",
                    "Metamorphose", "Malefices"]

class Professeur(Personne):
     def __init__(self, maison2, object_sort, vie_initial=150):

        self.vie_initial=vie_initial
        self.maison = maison2
        self.object_sort = object_sort

    point_fort = ["Malediction", "Enchantement",
                  "Metamorphose", "Malefices"]
    point_faible = ["Malediction", "Enchantement",
                    "Metamorphose", "Malefices"]