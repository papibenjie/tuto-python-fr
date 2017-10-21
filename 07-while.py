# Bon maintenant sa devient interressant !
# Les boucles vons nous servir a executer plusieurs fois le meme bout de code.
# Ici nous ne verrons que la boucle while mais sachez qu'il en existe une autre

# la boucle while s'utilise similairement au if mais il ne faut pas les confondre,...
# elles ne font pas du tout la meme chose

# While True:
#    print("Ce code s'execute sans jamais s'arreter !")

# While False:
#    print("Ce code ne s'execute jamais. ")


# Faisons un bout de code qui s'execute tant que l'utilisateur n'a pas entrer la valeur 'stop'

valeur = "go"
# n'importe quoi sauf "stop"
while valeur != "stop":
    print("Je m'execute! ")
    valeur = input("Entrer la valeur 'stop' pour arreter la boucle: ")


# dans les boucle on utilise souvant une variable int qu'on appelle increment....
# qui augmente de 1 a chaque iteration (tour) de boucle
# Imaginons que nous voulions afficher le mot "pomme" 10 fois a l'ecran.
# Nous pourrions ecrire 10 print l'un en dessous de l'autre mais avouez que cela n'est pas pratique..
# On nomme souvent l'increment 'i'
# On peut utiliser la notation suivante:
# i += 1 ---> i = i + 1

i = 0
while i < 10:
    print("pomme")
    # Ne pas oublier sinon on ne sort jamais de la boucle
    i += 1


# Essayons de demander un chiffre a l'utilisateur et d'afficher tout les nombre entier de 0 a ce chiffre
i = 0
a = int(input("Valeur: "))
while i < a:
    print(i)
    i += 1

# Remaquez que j'envoie directement le retour de input() a la fonction int()


# Finalement une derniere chose tres pratique avec la boucle while
# Dans le dernier fichier, on demandais a l'utilisateur de choisir une operation a effectuer.
# Si le choix etais invalide, on l'affichais a l'ecran et le programme se terminais
# La boucle while nous permet de redemander une valeur a l'utilisateur tant que le chois est invalide


choix = -1
while choix < 0 or choix > 3:
    choix = int(input("Choisissez entre 0 et 3: "))

print("Vous avez choisis")
print(choix)
