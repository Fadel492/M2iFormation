class House:
    def __init__(self, surface):

        self._surface = surface

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, value):
        self._surface = value

    def display(self):
        print(f"Je suis une maison, ma surface est de {self._value} m2")

    def get_surface(self):
        return self._surface

