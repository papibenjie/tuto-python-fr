import random


def choisirMot(mots):
    # cette fonction doit selectioner un mot aleatoire
    # dans la liste "mots"

    return random.choice(mots)


def motCache(mot):
    # cette foncion renvoie un string de "*" de meme
    # longueur que le mot: "allo" -> "****"

    return "*" * len(mot)


def demandeInput():
    # cette fonction retourne une lettre que l'utilisateur
    # choisira. (pas de nombre, pas de majuscule)
    a = raw_input("Choisissez une lettre: ")
    return a


def trouvePoses(lettre, mot):
    # trouve LES position de la lettre dans le mots
    # ex: trouvePoses("b", "baba") -> [0,2]
    poses = []
    for i, v in enumerate(mot):
        if v == lettre:
            poses.append(i)
    return poses


def remplaceLettre(lettre, motUtilisateur, poses):
    # met les lettres au bonne position dans le motUtilisateur
    # ex: remplaceLettre("a", "*****", [1,3]) -> "*a*a*"
    mot = list(motUtilisateur)
    for i in range(len(mot)):
        if i in poses:
            mot[i] = lettre
    return "".join(mot)


def afficheMot(mot):
    print(mot)
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
