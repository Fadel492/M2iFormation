from Personne import Personne


class Sorciere(Personne):
    object_sort=[0,1]
    def __init__(self, maison1, object_sort, vie_initial=100):

        self.vie_initial = vie_initial
        self.maison = maison1
        self.object_sort = object_sort

   
    