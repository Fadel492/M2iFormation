class Person:
    """ 
    –Créez une classe «Person»
    –Créez une classe «Student» et une autre classe «Teacher», les deux héritent de la classe «Person».
    –La classe «Student» aura une méthode publique «GoToClasses», qui affichera à l’écran «I’mgoingto class.».
    –La classe «Teacher» aura une méthode publique «Explain», qui affichera à l’écran «Explanationbegins». 
    En plus, il aura un attribut privé «subject» de type string.
    –La classe «Person» doit avoir une méthode «SetAge(intn)» qui indiquera la valeur de leur âge (par exemple, 15 yearsold).
    –La classe «Student» aura une méthode publique «DisplayAge» qui écrira sur l’écran «Myageis: XX yearsold».
    –Vous devez créer une autre classe de test appelée «Test» qui contiendra «Main» et:
    –Créez un objet Person et faites-lui dire «Hello»–Créer un objet Student, 
    définir son âge à 15 ans, faites-lui dire «Hello», «I’mgoingto class.» et afficher son âge
    –Créez un objet Teacher, 40 ans, demandez-lui de dire «Hello» puis commence l’explication.
    """

    def __init__(self, _age):
        self._age = _age

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value


class Student(Person):
    def go_to_classes(self):
        print("I am going to classe")


class Teacher(Person):
    subject = ''

    def expalin(self):
        print("Hello: Explanation begins")
