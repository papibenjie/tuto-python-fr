# Ces fonctions simples doivent etre coder

# fonctions sur les listes
# Les fonction suivantes sont deja disponible dans python ! (max, min, sum)
# Il faut recoder les fonctions sans utiliser les fonctions deja presente


def maxi(liste):
    # cette fonction retourne le nombre maximum de la liste
    maxVal = liste[0]
    for i in liste:
        if i > maxVal:
            maxVal = i
    return maxVal


def mini(liste):
    # cette fonction retourne le nombre minimum de la liste
    minVal = liste[0]
    for i in liste:
        if i < minVal:
            minVal = i
    return minVal


def total(liste):
    # cette fonction retourne le total de la liste
    tot = 0
    for i in liste:
        tot += i
    return tot


if __name__ == '__main__':
    l = [1, 4, 6, 3, 2, 4]
    print("max: {0} = {1}".format(maxi(l), max(l)))
    print("min: {0} = {1}".format(mini(l), min(l)))
    print("tot: {0} = {1}".format(total(l), sum(l)))
