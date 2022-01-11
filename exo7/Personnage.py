class Personnage():
    def __init__(self, nom):
        self._nom = nom

    def display(self):
        return f'je me nome {self._nom}'