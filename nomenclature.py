# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:40:12 2022

@author: Théodore
"""
# schema = [
#     ["", "c|", "d|", "", "b|"],
#     ["a-", "a-", "a-", "a-", "a"],
#     ["", "", "", "", "e"]
# ]

schema = [
    ["a-", "a|", "", "", ""],
    ["b-", "a-", "a-", "a-", "a"],
    ["", "c", "d|", "", ""],
    ["", "", "d", "", ""]
]

plus_longue = "a"
famille = "alcane_ram"
longueurs = {}

signes = "-|"

noms = {
    "alcane": {1: "méth",
               2: "éth",
               3: "prop",
               4: "but",
               5: "pent",
               6: "hex",
               7: "hept",
               8: "oct",
               9: "non",
               10: "déc"
               },
    "préfixe": {2: "di",
                3: "tri",
                4: "tétra"}
}
noms["alcane_ram"] = noms["alcène_ram"] = noms["alcène"] = noms["alcane"]
noms["alcool"] = noms["acide_carboxylique"] = {}
for i in range(1, 11):
    noms["alcool"][i] = noms["alcane"][i]+"an"
    noms["acide_carboxylique"][i] = "acide "+noms["alcane"][i]+"ano"

fin_noms = {"alcane": "ane",
            "alcane_ram": "yl",
            "alcène": "ène",
            "alcène_ram": "ol",
            "acide_carboxylique": "ïque"}

for lignes in schema:
    for colonnes in lignes:
        case = colonnes.strip(signes)
        if case != "":
            if case not in longueurs:
                longueurs[case] = 0
            longueurs[case] += 1


distances_ramif = {}
for i in longueurs.keys():
    if i != plus_longue:
        distances_ramif[i] = 0

#print(longueurs)


def determiner_distances():
    """
    The determiner_distances function finds the distance between each point in a string of characters.
    It does this by finding the closest point to each character, and then adding 1 to that distance.
    The function returns a list of distances.
    
    :return: The size of the longest determiner on the schema
    :doc-author: Trelent
    """
    x = y = 0
    taille_branche_princip = 0
    fin = False
    while not fin:
        cherche = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]  # ,(y-1,x-1),(y+1,x+1)]
        x_suivant = y_suivant = 0
        case = schema[y][x]
        if case != "":
            if case == plus_longue:
                fin = True
                taille_branche_princip += 1
            elif plus_longue in case:
                if "-" in case.strip(plus_longue):
                    if x+1 < len(schema[0]) and schema[y][x+1].strip(signes) == plus_longue:
                        x_suivant = 1
                        taille_branche_princip += 1
                        #cherche.remove((y, x+1))
                elif "|" in case.strip(plus_longue):
                    if y+1 < len(schema) and schema[y+1][x].strip(signes) == plus_longue:
                        y_suivant = 1
                        taille_branche_princip += 1
                        #cherche.remove((y+1, x))
                if not fin and y_suivant == x_suivant == 0:
                    fin = True
                    print("La chaîne est coupée")
            else:
                x_suivant = 1
                if x+x_suivant == len(schema[0]):
                    x = 0
                    x_suivant = 0
                    y_suivant = 1
                    if y+y_suivant == len(schema):
                        fin = True

        else:
            x_suivant = 1
            if x+x_suivant == len(schema[0]):
                x = 0
                x_suivant = 0
                y_suivant = 1
                if y+y_suivant == len(schema):
                    fin = True

        x += x_suivant
        y += y_suivant
        test_branche_autour(cherche, taille_branche_princip, x, y)
    return taille_branche_princip


def test_branche_autour(cherche, dist, x, y):
    #print("coucou")
    #print(cherche)
    for i in cherche:
        if 0 <= i[0] < len(schema) and 0 <= i[1] < len(schema[0]):
            #print(schema[i[0]][i[1]])
            case = schema[i[0]][i[1]]
            case_coupe = case.strip(signes)
            #print(i, (y, x))
            if case_coupe != plus_longue and case_coupe in distances_ramif and distances_ramif[case_coupe] == 0:
                #print("-" in case and i == (y, x-2), "|" in case and i == (y+1, x-1), "-" not in case and "|" not in case)
                if ("-" in case and i == (y, x-2)) or ("|" in case and i == (y+1, x-1)) or ("-" not in case and "|" not in case):
                    distances_ramif[case_coupe] = dist
                    #print(dist, case_coupe)


def ordre(dict_dist):
    maximum = minimum = list(dict_dist)[0]
    for i in dict_dist:
        if dict_dist[i] < dict_dist[minimum]:
            minimum = i
        if dict_dist[i] > dict_dist[maximum]:
            maximum = i
    if dict_dist[minimum] < longueurs[plus_longue]-dict_dist[maximum]-1:
        for i in dict_dist:
            dict_dist[i] = longueurs[plus_longue]-dict_dist[i]
    return dict_dist


def ranger(tab):
    for i in range(len(tab)):
        j = i

        while j > 0 and tab[j][0] > tab[j-1][0]:  # noms[famille][longueurs[tab[j][0]]] < noms[famille][longueurs[tab[j-1][0]]]:
            valeur = tab[j]
            tab[j] = tab[j-1]
            tab[j-1] = valeur
            j -= 1

    return tab


assert determiner_distances() == longueurs[plus_longue], "Les longueurs ne correspondent pas"
distances_ramif = ordre(distances_ramif)
tab_nomenclature = list(distances_ramif)
tab_nomenclature = ranger(tab_nomenclature)
#print(tab_nomenclature)
tab_suppr = []
nomenclature = ""
for indice, valeur in enumerate(tab_nomenclature):
 #   print(valeur)
    if valeur not in tab_suppr:
        prefixe = ""
        nb = 0
        nb_ram = str(distances_ramif[valeur])
        for j in tab_nomenclature:
            #            print(j,distances_ramif[j])
            if longueurs[j] == longueurs[valeur]:
                tab_suppr.append(j)
                nb += 1
                if nb > 1:
                    nb_ram += (","+str(distances_ramif[j]))
        if nb > 1:
            prefixe = noms["préfixe"][nb]
        if indice > 0:
            nomenclature += "-"
#        print(valeur, longueurs[valeur], nb, tab_suppr, valeur in tab_suppr)
        nomenclature += nb_ram+"-"+prefixe+noms[famille][longueurs[valeur]]+fin_noms[famille]
nomenclature += noms["alcane"][longueurs[plus_longue]]+fin_noms["alcane"]
print(nomenclature)

#for i in schema:
#    print(i)
