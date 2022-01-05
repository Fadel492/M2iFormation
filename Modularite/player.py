def parler(personnage,message):
    """
    module qui permet a la personne de parler

    Args:
        str (personnage): 
        str (message): 

    """
    print(f"{personnage} dit: {message}")




def au_revoir():
    """
    permet d'afficher au revoir

    """
    print("Au revoir les amis")


if __name__ == "__main__":

    """
    PHASE de Test de tout vos module de vos propre test
    avant de le mettre dans le programme principale
    """
    
    parler("jason","Bonjour tout le monde")
    au_revoir()
