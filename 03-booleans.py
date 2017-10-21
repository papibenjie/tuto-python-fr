# les variables de type boolean sont tres utiles !
# se sont elles qui nous permmettront de controller les conditions et meme les boucles

# ces variables ne peuvent avoir que 2 etat : True ou False

# on peut creer une de ces variables en comparant d'autres valeurs ou variables
# pour cela il faut utiliser les operateurs booleans (<,>,==,!=,<=,>=,not)

# ------------------------------------------------------
a = 10 < 10  # a = False

a = 10 <= 10  # a = True

a = 4 == 4  # a = True

a = 4 != 7  # a = True

# etc..


# ------------------------------------------------------
# Bon.. maintenant abordons un aspect plus complexe
# Il es possible de combiner les operateur boolean ensemble
# Pour cela il existe d'autres operateurs (not, and, or, ...)

# ------------------------------------------------------
# L'operateur not sert a inverser la valeur d'un boolean

a = not True  # a = False

# ------------------------------------------------------
# Pour que l'operateur 'and' (et) sois True, toutes les valeurs compare doivent etre True

a = True and True  # a = True

a = False and True  # a = False

a = False and False  # a = False

a = True and True and False  # a = False

a = True and True and True  # a = True

# ------------------------------------------------------
# Pour que l'operateur 'or' (ou) sois True, au moin une des valeurs compare doit etre True

a = True or True  # a = True

a = False or True  # a = True

a = False or False  # a = False

a = True or True or False  # a = True

a = False or False or False  # a = False


# ------------------------------------------------------
# Bon maintenant essayons de combiner tous sa
# Imaginons que nous voulons savoir si nous devons acheter un article
# si le prix est au dessus de 10$ nous n'achetons pas
# sinon on achete
# la variable 'achete' doit etre True SI on achete sinon False
# Remarquez l'utilisation du mot SI ;) nous y reviendrons plus tard

prix = 20
achete = prix < 10
print(achete)

prix = 5
achete = prix < 10
print(achete)
