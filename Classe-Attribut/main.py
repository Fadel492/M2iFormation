# class Humain:
#     """
#     classe des etres humains

#     """
#     humain_creer=0      # attribut de la classe different du constructeur

#     def __init__(self,c_prenom,c_age):  # constructeur permet d'initialiser plus facile la classe
#         print("creation d'un humain.......")
#         self.prenom=c_prenom
#         self.age=c_age
#         Humain.humain_creer+=1

# print("Lancement de programme !:")

# print(f"Humain creer est initialment est a {Humain.humain_creer} !:")

# h1=Humain("fadel",12)  # instanciation et appel aux attribut
# print(f"prenom de h1 est {h1.prenom} et son age est {h1.age} ans")
# print(f"Humain creer passe de {Humain.humain_creer}")

# h2=Humain("Henry",5)
# print(f"prenom de h2 est {h2.prenom} et son age est {h2.age} ans")
# print(f"Humain creer passe de {Humain.humain_creer}")
# # h2.prenom="Ouleye"    la modification peut se faire sans mettre de seteur
# # print(f"changement du prenom de h2 est {h2.prenom} et son age est {h2.age} ans")

class Voiture():

    def __init__(self, mark):
        self.mark = mark

    def __str__(self):
        print(f"la mark de ma voiture est   {self.mark}")


Mavoiture = Voiture("peugeot")
print(Mavoiture)
# le print appelle direct la fonction str
