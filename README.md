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
 ## Exercice Combat

Créer un jeu de combatCréer une interfacepersonnage
•Point de vie (générer aléatoirement entre 100 et 200 pointsde vie)
•Arme
•Nom
•Cible
•Attaquer()
•Cibler()
Créer une classe abstraite personnage qui implémente l’interfaceCréer une classe«gentil» qui hérite de AbstractPersonnage
•Soin()Créer une classe méchant qui hérite de AbstractPersonnage
•Création de nom aléatoire()
Créer une classe Arme pour équiper les personnages
•Dégâts (générer aléatoirement)
Créer un classe Combat qui gère les combats au tour par tour Créer une classe partie qui met en place les personnages et qui lance le combatFaire marcher le toutRemplacer les personnages pour le combat par des équipes avec ciblage aléatoireRemplacer les dégâts de l’arme par des plages de dégâtsCréer des armes qui hérite d’Arme et qui amènentdes éléments particuliersDans Gentil 
rajouter une variable classe et qui modifie les valeurs des variablesDans Arme rajouter des chances de coup critiques.

## Exercice 

Jeu de désLe but de l'exercice est de créer un jeu de __dés__ classique dans lequeldes joueurs joueront àtour de rôle enlançant un gobelet, qui contiendra des dés. 
Au bout d'un certain nombre de tour, On désigne le gagnant.
Le gagnant est le joueur qui a le score le plus élevé. 
Pour cela nous allons devoir définir plusieurs classes :
Classe DéLa classe Déest celle qui représente un De du gobelet.
Celle-ci a:
-Unattribut :
-Valeur: 
un nombre représentant la valeur d'un lancerde déUn constructeur:
-Sansarguments 
-Quiinitialise la valeur du dé à 0Ainsi que 2méthodes :
-get_valeur() : renvoie la valeur du dé
-lancer() : change la valeur du dé ->cette valeur doit être un nombre généré aléatoirement entre 1 et 6Classe GobeletLa classe Gobelet représente le gobelet utilisédans la partie
.Celui-ci a:
Deuxattributs :
-Valeur: nombre représentant la valeur d'un lancerdu gobelet
-Des: tableau de dés qui contient un certain nombre de dés
-Un constructeur 
-Avecun argument oconstructor(nb_des) : initialise la valeur du gobelet à 0, génère le nombre de dés nécessaires à lapartie et les ajoute au tableau desAinsi que 3 méthodes :
-get_valeur() : renvoie la valeur du gobelet
-lancer() : change la valeur des dés du gobelet ; met à jour la valeur du gobelet
-afficher_score() :affiche en console le score du dernier lancé de gobelet
Classe JoueurLa classe Joueur représente une personne participant àla partie :
Celui-ci à
:Deuxattributs :
-Nom: chaîne de caractères représentant le nom du joueur-Score: nombre représentant le score du joueur (à un instant t)Un constructeur:
-Avecun argument oconstructor(nom) : initialise la valeur du nom du joueur à partir du paramètre nom, initialise le scoredu joueur à 0Ainsi que 4méthodes :
-get_nom() : renvoie le nom du joueur
-get_score() : renvoie le score du joueur
-jouer(gobelet) : prend en paramètre le gobelet de la partie, lance le gobelet, met à jour le score dujoueur en fonction du résultat du lancé
-afficher_score() : affiche en console le score du joueurClasse PartieLa classe Partie représente une partie de dés.Celui-ci à:
Troisattributs :
-joueurs : tableau de joueurs
-nb_tours : entier représentant le nombre de tours à jouer-gobelet : gobelet de dés
-Un constructeur:
-Avecdeuxarguments oconstructor(nb_tours, nb_des) : crée l'objet Partie en récupérant le nombre de tours et nombre de désAinsi que 3méthodes :
-initialiser() : permet d'inscrire des joueurs dans la partie
-lancer() : lance la partie : chaque joueur joue à tour de rôle pendant les n tours. Une fois lapartieterminée, affiche le gagnant.
-afficher_gagnant() : compare les scores des joueurs et affiche le gagnant.Libre à vous de demander au lancement de la partie le nombre de dés, le nombre detours et lenom des participantsou de les définirdans le code