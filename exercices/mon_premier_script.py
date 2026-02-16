#bon je connais déjà le python perso donc je vais accélérer et faire les tests directement

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = 0
for prenom in prenoms:
    if len(prenom) > 7:
        more_than_seven += 1
        print(prenom + " > à 7 lettres")
    else:
        print(prenom + " < à 7 lettres")
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(more_than_seven))