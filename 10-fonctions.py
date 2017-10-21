# Les fonctions sont un concept fondamental de programmation.
# Il nous sert a encapsuler certain bout de code que l'on peut...
# reutiliser un peut partout dans notre programme

# Une fonction se declare avec le mot def
# ensuite on decide du nom de la fonction et on defini les parametre si il y en a


def hello():
    print("hello")

# Cela declare une fonction mais ne l'execute pas. c'est comme avec la fonction print
# il faut l'appeller pour l'executer


hello()  # -> "hello"

# on peut definir des parametre que la fonction recevra.
# comme la fonction print qui prend une chaine de character en parametre


def addition(a, b):
    print(a + b)


# on peut desormais appeller la fonction addition() en envoyant le parametre que l'on veut
addition(2, 5)  # -> 7


# finalement, une fonction peut retourner une ou plusieurs valeur
# redefinissons la fonction additions pour qu'elle retourne le resultat au lieu de l'afficher

def addition(a, b):
    resultat = a + b
    return resultat

# Remarque l'utilisation du mot return, il stop la fonction et retourne la valeur desire


print(addition(2, 5))  # -> 7


# On peut retourner plusieurs valeurs
def division(a, b):
    div = a // b
    mod = a % b
    return div, mod


print(division(10, 3))  # -> (3, 1)


# La fonction max() recois une liste en parametre et renvois le plus grand element de celle-ci
# Essayons de recoder cette fonction par nous meme.
# Nous l'appellerons maxi()

def maxi(l):  # Je recois ma liste en parametre
    maxnb = l[0]   # Je defini le plus grand nombre trouver comme etant le premier nombre de ma liste pour le moment
    for i in l:  # Je parcours ma liste
        if i > maxnb:  # Si le nombre que je verifie est plus grand que le plus grand nombre a date
            maxnb = i  # je redefini le plus grand nombre

    # Une fois que la liste a ete parcouru, maxnb sera egal au plus grand nombre de ma liste
    return maxnb


a = [1, 4, 2, 6, 1]
print(maxi(a))
