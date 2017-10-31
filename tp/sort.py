# Ces fonctions de tri doivent etre recoder.abs
# dans python la fonction sort() existe mais nous la recoderons

# Tri a bulle.
# Cet algo est un es plus simple mais il n'est pas tres performant.

# Pour chaque nombre dans la liste, on compare avec tout les autres nombres.
# Si le nombre comparer est plus petit, on inverse la position des 2 abs

# la fonction ne retourne rien, elle modifie la liste directement
def bubble(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i] < liste[j]:
                liste[i], liste[j] = liste[j], liste[i]



if __name__ == '__main__':
    l = [3, 6, 2, 3, 6, 7, 1]
    bubble(l)
    print(l) # -> 1, 2, 3, 3, 6, 6, 7
