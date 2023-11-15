def est_vide(chaine):
    return not bool(chaine)

# Exemple d'utilisation
chaine = "Hello"
if est_vide(chaine):
    print("La chaîne est vide.")
else:
    print("La chaîne n'est pas vide.")

