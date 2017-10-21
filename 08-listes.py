# Maintenant nous allons decouvrir un nouveau type de variable, les liste !

# Les liste sont en veriter un suite de variable qui peuvent etre de tout type.
# generalement, les variables dans une liste sont toute de meme type...
# mais sachez que il est possible quand meme de mixer les type dans une liste.

# On declare des liste comme des variable mais en utilisant les crochets ( [] )

a = [99, 7, 4]
print(a)  # [99,7,4]

# On peut ensuite acceder a chaque element de la liste individuelement un utilisant un index..
# qu'on met entre crochet apres le nom de la variable.
# Attention, l'index commence a 0

print(a[0])  # 99
print(a[1])  # 7
print(a[2])  # 4
# print(a[3])  # IndexError: list index out of range



# Voici quelque fonctions qui nous permmettent de manipuler des listes

len(a)  # retourne la longueur de la liste -> 3
max(a)  # retourne la valeur maximum de la liste -> 4
min(a)  # retourne la valeur minimum de la liste -> 1
