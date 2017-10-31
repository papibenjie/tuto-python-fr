# Seule les fonctions doivent etres complete


import random


def choisirMot(mots):
    # cette fonction doit selectioner un mot aleatoire
    # dans la liste "mots"

    return "mot aleatoire"


def motCache(mot):
    # cette foncion renvoie un string de "*" de meme
    # longueur que le mot: "allo" -> "****"

    return "*************"


def demandeInput():
    # cette fonction retourne une lettre que l'utilisateur
    # choisira.
    return "b"


def trouvePoses(lettre, mot):
    # trouve LES position de la lettre dans le mots
    # ex: trouvePoses("b", "baba") -> [0,2]

    return [0]


def remplaceLettre(lettre, motUtilisateur, poses):
    # met les lettres au bonne position dans le motUtilisateur
    # ex: remplaceLettre("a", "*****", [1,3]) -> "*a*a*"
    return "a**a*"


def afficheMot(mot):
    # doit afficher le mot
    pass



if __name__ == '__main__':

    mots = ["chien", "chat", "abeille", "minou"]

    mot = choisirMot(mots)
    motUtilisateur = motCache(mot)

    while mot != motUtilisateur:
        afficheMot(motUtilisateur)
        lettre = demandeInput()
        poses = trouvePoses(lettre, mot)
        motUtilisateur = remplaceLettre(lettre, motUtilisateur, poses)

    print(mot)
