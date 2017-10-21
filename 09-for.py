# le for est une boucle comme le while.
# par contre, il ne se fie pas sur une condition pour verifier si il doit continuer.
# le for utilise un iterateur. nous y reviendrons plus tard mais sachez qu'une liste en est un

# imaginons que nous ayons une liste et que vous voulions afficher chaque nombre...
# de cette liste multiplier par 2

a = [1, 3, 5, 7]

# Utilisons le for pour parcourir cette boucle
for i in a:
    # A chaque iteration de boucle, la variable i prendra une valeur de la liste 'a' ..
    # jusqu'a la fin de la liste et s'arretera
    print(i * 2)


# La fonction range()
# cette fonction est tres utile. elle nous permet de creer un iterateur...
# qui part de 0 jusqua la valeur souhaite
# cette fonction est tres pratique quand on souhaite executer une boucle un nombre d'iteration determiner.
# la boucle while servira plutot quand le nombre d'iteration est indetermine

# affichons 10 foix le mot pomme a l'ecran
for i in range(10):
    print("pomme")
