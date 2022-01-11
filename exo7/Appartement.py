from House import House
class Appartement(House):
    def __init__(self, surface):
        super().__init__(surface)
        
    def display(self):
        return f'je suis un appartement et ma surface est {super().get_surface()}'
