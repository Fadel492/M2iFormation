# POO  

## Expliquation de quelques notions

* _Classe_: structure de donnée
* _methode_: fonction de la classe
* _instance_ de la classe nom classe ou objet tt cours =instancier veut creer un objet
* _Attribut_: variable de la classe ou champs
* objet: ensemble de donnée à une classe

## Synthese  

* Mettre du code python grace a des accents grave altgr+7
* Exemple ci dessous
* _code_  
``
print("hello word")
``
* self nous permet d'aller sur le numero de la ligne donc à chaque fois qu'on cree une instance self nous permet de nous deplacer sur le numero de la ligne

## Bonne ptratique

* module_name 
* package_name 
* ClassName
* method_name
* ExceptionName
* function_name
* GLOBAL_CONSTANT_NAME
* global_var_name
* instance_var_name
* function
* parameter_name
* local_var_name  

## Heritage + methode str et rpr

````
    class Voiture:  
        def __init__(self,mark):  
            self.mark=mark
    
    def __str__(self):
        print("la mark de ma voiture est + self.mark)


La fonction print appelle directement __str__
var=property(get_variable,set_variable) est un sucre syntaxique nous permet de nous implifier la vie

Méthode 1 : utilisation get / set

* Getter / accesseur  


 def get_nom(self):

    return self._nom.capitalize()

* Setter/mutateur


def set_nom(self, value):
    if type(value) is str:  
         self._nom = value
     else:
         pass



* Méthode 2: utilisation des properties

     def get_nom(self):
         return self._nom

     def set_nom(self, value):
         self._nom = value

     nom = property(get_nom, set_nom)


 class Utilisateur:  
 
     def __init__(self, nom, prenom):
         self._nom = nom
         self._prenom = prenom

     * Getter avec annotation property  
     @property
     def nom(self):
         return self._nom

     @nom.setter
     def nom(self,value):
         self._nom = value

 utilisateur = Utilisateur("timio", "Thomas")

 utilisateur.nom = "Coucou"
 print(utilisateur.nom)
 ````
 