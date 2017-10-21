# Essayons de faire un programmes plus complexe, en combinant se que nous savons pour le moment.

# Le programme se fera en 3 temps.
# Premierement, nous demanderons deux valeurs a l'utilisateur. a et b
# Deuxiemement, nous demanderons a l'utilisateur se qu'il desire faire avec ces deux valeurs (+,-,*,/)
# Finalement, nous afficherons le resultat de l'operation

a = input("Valeurs 1: ")
b = input("Valeurs 2: ")
# Attention ces valeurs sont des characteres

a = int(a)
b = int(b)


print("1. '+' ")
print("2. '-' ")
print("3. '*' ")
print("4. '/' ")
choix = input("Choix: ")
choix = int(choix)

print(choix)

if choix == 1:
    resultat = a + b
elif choix == 2:
    resultat = a - b
elif choix == 3:
    resultat = a * b
elif choix == 4:
    resultat = a / b
else:
    resultat = "Erreur, entre invalide"

print("Le resultat est: ")
print(resultat)
