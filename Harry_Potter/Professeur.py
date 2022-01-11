from Personne import Personne


class Professeur(Personne):
     def __init__(self, maison2, object_sort, vie_initial=150):

        self.vie_initial = vie_initial
        self.maison = maison2
        self.object_sort = object_sort

   