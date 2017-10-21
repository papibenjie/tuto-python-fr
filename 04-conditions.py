# Les conditions sont geniales!
# ELles nous permmettent d'executer certaina bouts de code conditionnellement

# Les conditions s'utilisent avec les mot 'if, else et elif' et une indentation qui definie le bout de code a executer

# ------------------------------------------------------
# If prend en parametre une valeur boolean
if True:
    print("Ce code est toujours execute")

if False:
    print("Ce code n'est jamais execute")

# reprenons l'exemple du dernier fichier
# si en dessus le prix es en dessous de 10$ on achete !
prix = 20
if prix < 10:
    print("J'achete !")


# on peut enchainer les condition
prix = 20
if prix < 10:
    print("J'achete !")
if prix >= 10:
    print("Je n'achete pas !")


# ------------------------------------------------------
# elif s'utilise a la suite d'in if. la condition ne sera verifie que si le if precedant est False
prix = 20
if prix < 10:
    print("J'achete !")
elif prix >= 10:
    print("Je n'achete pas !")

# ------------------------------------------------------
# else est comme le elif sauf qu'il ne prend pas de condition
# il execute peut importe, si le if precedans est False
prix = 20
if prix < 10:
    print("J'achete !")
else:
    print("Je n'achete pas !")

# ------------------------------------------------------
# Imaginons que si le prix est de 10$ on essais de negacier le prix
prix = 10
if prix < 10:
    print("J'achete !")
elif prix > 10:
    print("Je n'achete pas !")
else:
    print("Je negocie !")


# ps: vous souvenez vous du modulo ? oui! oui! celui que vous pensez inutile..
#    detrompez-vous, on s'en sert souvent pour verifier si un nombre est mutiple d'un autre

# if nb % 2 == 0:
#   print("La valeur dans nb est divisible par 2 donc pair")
