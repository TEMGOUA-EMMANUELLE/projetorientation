#coding: utf-8

import numpy as np
import pandas as pd

"""
NB: gc    -> Génie Civile
    gi    -> Génie Informatique
    get   -> Génie Electriue et Télécom
    gmind -> Génie Industriel et mécanique
"""

# Le nombre d'étudiants par spécialités suivant la repartition effectuée par l"école
nb_etud_gc = 155  
nb_etud_gi = 150
nb_etud_get = 80
nb_etud_gmind = 58

colums = ["Spécalités", "Informatique 1", "Electromagnétisme 1", "Mécanique 1", "Elément de chimie", "Trvaux pratiques de physique 1", 
          "Algèbre générale", "Analyse réelle 1", "Technologies et sciences des matériaux", "Electromagnétisme 2", "Informatiue 2", 
          "Analyse réelle 2", "Algèbre linéaire", "Géométrie affine et euclidienne", "Informatique 3", "Probabilités et statistiques", 
          "Electrocinétiques", "Mécanique 2", "Trvaux pratiues de physique 2", "Séries et intégrales", 
          "Algèbre multilinéaire, courbes et surfaces", "Circuits électriques et électrocinétique", "Optique géométrique", "Thermodynamique", 
          "Statique", "Informatique 4", "Analyse dans les espaces vectoriels de dimensions finies", "Analyse numérique"]

# Poids des différentes UEs par spécialités (4 étant le maximum et 1 le minimum)
# l'ordre est celui des colonnes ci-dessus en commencant par Informatique 1
weights_gc = [2, 2, 4, 2, 2, 4, 4, 4, 2, 2, 4, 4, 4, 2, 3, 2, 4, 2, 4, 4, 1, 2, 3, 4, 2, 4, 4]
weights_gi = [4, 2, 1, 1, 2, 4, 3, 1, 2, 4, 4, 4, 3, 4, 4, 2, 1, 2, 3, 3, 2, 2, 1, 1, 4, 2, 3]
weights_get = [3, 4, 1, 1, 4, 3, 3, 1, 4, 3, 2, 3, 2, 3, 3, 4, 1, 4, 2, 2, 4, 3, 3, 1, 3, 1, 4]
weights_gmind = [3, 3, 3, 2, 4, 3, 3, 4, 4, 3, 3, 3, 2, 3, 2, 4, 1, 4, 2, 2, 4, 2, 4, 3, 3, 2, 4]

def generateSigleData(nb_etudiant, weights, specialite):

    columns = []
    for _ in range(nb_etudiant):

        column = [specialite]
        for w in weights:
            column.append(np.random.randint(10 + w*1.25 , 10 + 2.5 * w))
        columns.append(column)

    columns = np.array(columns)
    return columns

def generateDataset():

    data_gc = generateSigleData(nb_etud_gc, weights_gc, "Génie Civile")
    data_gi = generateSigleData(nb_etud_gi, weights_gi, "Génie Informatique")
    data_get = generateSigleData(nb_etud_get, weights_get, "Génie Electrique et Télécom")
    data_gmind = generateSigleData(nb_etud_gmind, weights_gmind, "Génie Industriel et Mécanique")

    data = np.concatenate((data_gc, data_gi, data_get, data_gmind), axis=0)
    data = pd.DataFrame(data, columns=colums)

    return data