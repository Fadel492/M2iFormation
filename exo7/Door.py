class Door():
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    
    def display(self):
        return f'je suis une porte et ma couleur est {self.color}'

