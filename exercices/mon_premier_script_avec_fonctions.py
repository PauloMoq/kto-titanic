import unittest

"""
Count names with more than seven letters
"""
def names(prenoms:list) -> int:
    """
    Fonction qui prend en paramètre une liste de string, et qui indique, pour chacun, 
    si l'élément contient plus de 7 caractères, ou non.

    Args:
    - prenoms : param(list[str])
    - more_than_seven : return(int) 
    """
    more_than_seven = 0 #compteur qu'on va return

    for prenom in prenoms: #parcours de la liste prenoms
        if len(prenom) > 7:
            more_than_seven += 1 #incrément du compteur
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7") #prenom>7
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7") #prenom<7
    return more_than_seven

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(names(prenoms=prenoms)))

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"] #exemple de liste
        more_than_seven = names(prenoms=prenoms) #appel fonction
        self.assertEqual(more_than_seven, 4) #test réel (OK/KO)

if __name__ == '__main__':
    unittest.main() #on lance le test à l'exécution du fichier