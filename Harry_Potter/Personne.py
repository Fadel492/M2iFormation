class Personne:

    point_fort = ["Malediction", "Enchantement",
                  "Metamorphose", "Malefices"]
    point_faible = ["Malediction", "Enchantement",
                    "Metamorphose", "Malefices"]
    def __init__(self, nom, prenom, age, vie,point_fort,point_faible):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.vie = vie
        self.point_fort=point_fort
        self.point_faible=point_faible