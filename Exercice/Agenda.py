class Contact:
    """ 
    Ecrire un programme qui permet de tenir un Agenda
    - Un agenda comporte des contacts
    - Un contact est défini par un nom, un prénom, un numero de tél, un mail et une adresse 
        (numéro de rue, rue, code postal, ville)
    - Au moment de son entrée dans l’agenda, un contact a au minimum un nom
    - Les informations de contact doivent passer par une validation des données
    - L’agenda, permet d’ajouter, de modifier et de supprimer des contacts
    - On peut aussi afficher les détails du contact d’une façon formatée
    - On peut aussi afficher l’agenda en entier par ordre alphabétique en passant 
        en paramètre l’attribut sur lequel se fait le tri
    - L’agenda offre aussi un sommaire qui contient tous les noms de tous les contacts 
        (ne pas oublier le cas de la modification et de la suppression d

    """

    def __init__(self, nom, prenom, tel, mail, adresse):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail
        self.adresse = adresse


class Agenda(Contact):
    def ajouContact(self, nom, prenom, tel, mail, adresse):
        self.nom = self.nom + nom
        self.prenom = self.prenom + prenom
        self.tel = self.tel + tel
        self.mail = self.mail + mail
        self.adresse = self.adresse + adresse

    def modifier_contact(self, nom, prenom, tel, mail, adresse):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail
        self.adresse = adresse
        return self.nom, self.prenom, self.tel, self.mail, self.adresse

    def suprimer_contact(self, nom, prenom, tel, mail, adresse):
        del(self.adresse)
        del(self.nom)
        del(self.tel)
        del(self.mail)
        del(prenom)

    def tri_contact(self, nom):
        self.nom.sort()
