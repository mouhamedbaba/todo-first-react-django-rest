def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)

def verifier_victoire(plateau, joueur):
    # Vérifier les lignes et les colonnes
    for i in range(3):
        if all(plateau[i][j] == joueur for j in range(3)) or all(plateau[j][i] == joueur for j in range(3)):
            return True

    # Vérifier les diagonales
    if all(plateau[i][i] == joueur for i in range(3)) or all(plateau[i][2 - i] == joueur for i in range(3)):
        return True

    return False

def jouer_tic_tac_toe():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueurs = ["X", "O"]
    tour = 0

    while True:
        afficher_plateau(plateau)
        joueur_actuel = joueurs[tour % 2]
        print(f"C'est au tour du joueur {joueur_actuel}")

        ligne = int(input("Entrez le numéro de ligne (0, 1, 2) : "))
        colonne = int(input("Entrez le numéro de colonne (0, 1, 2) : "))

        if plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = joueur_actuel
            if verifier_victoire(plateau, joueur_actuel):
                afficher_plateau(plateau)
                print(f"Le joueur {joueur_actuel} a gagné !")
                break
            elif all(plateau[i][j] != " " for i in range(3) for j in range(3)):
                afficher_plateau(plateau)
                print("Match nul !")
                break
            tour += 1
        else:
            print("La case est déjà occupée. Choisissez une autre case.")

if __name__ == "__main__":
    jouer_tic_tac_toe()
