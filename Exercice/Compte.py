class Compte:

    """ 
    Ecrire une classe compte bancaire qui a pour attribut un numero de compte, un nom de client, le solde, 
    le nombre d’opérations réalisées et une variable de classe nb max d’opérations
    - Ecrire le constructeur du compte
    - Ecrire les getters
    - Ecrire la représentation graphique sous la forme « nom : xxx, numCpte : yyy, solde : 100, nbreOp : 3 »
    - Ecrire une méthode versement qui gère les versements
    - Ecrire une méthode retrait qui gère les retraits (notamment s’assure que le compte est suffisamment provisionné)
    - Ecrire une méthode virement qui permet d’envoyer de l’argent en renseignant le numéro de compte de destination
    - Ecrire une méthode frais qui applique des frais à hauteur de 1% de l’opération pour chaque opération 
    en plus du nb max d’opérations par compte ➔ Les frais s’appliquent à tous type d’opération hormis l’affichage du compte
    """
    max_op: int = 0   # lisibilite

    def __init__(self, numero, nom, solde, operation):
        self.numero = numero
        self.nom_client = nom
        self.solde = solde
        self.operation = operation

    def get_numero(self):
        return self.numero

    def get_nomc(self):
        return self.nom

    def get_solde(self):
        return self.solde

    def get_op_realise(self):
        return self.operation

    def versement(self, solde, numero):
        print(
            f"Versement de {solde} euro en cours sur ce compte compte ...")
        if(self.numero == numero):
            self.solde = self.solde + solde
        else:
            print("le numero de compte saisie est invalide")
        return self.solde

    def retrait(self, solde):
        if(self.solde <= solde):
            print("La somme que vous voulais retiré est superieur à votre solde")
            print("Veuillez choisir un montant plus petite")
        else:
            print(
                f"vous avez retire {solde} et il vous reste {self.solde-solde} dans votre compte")

    def virement(self, numero, solde):
        print(f"Virement de {solde} euro sur IBAN {numero} ...")
