from Harry_Potter.Personne import Personne


class Sort(Personne):
    def __init__(self, nom, couleur_sort, categorie, degats, vie):
        self.nom = nom
        self.couleur_sort = couleur_sort
        self.degats = degats
        self.vie = vie


    def sort_soin(self, object_sort, vie):
        if (object_sort == 1):
            return self.vie_initial+1

    def tomber(self,object_sort):

        if (object_sort == 1):
            self.vie = self.vie_initial-1


   

        

