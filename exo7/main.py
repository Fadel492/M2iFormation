from House import House
from Door import Door
from Personnage import Personnage
from Appartement import Appartement

personnage=Personnage("fadel")
print(personnage.display())

door=Door("Bleu")
print(door.display())

appartement=Appartement(50)
print(appartement.display())
