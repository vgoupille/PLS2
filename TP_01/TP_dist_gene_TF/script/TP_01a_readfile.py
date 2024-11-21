import sys
import pprint  # module pour afficher des données de manière plus lisible

filename = sys.argv[1]
# liste des arguments passés en ligne de commande (argv[0] est le nom du script), argv est une liste


# creation d'un dictionnaire pour stocker les positions des gènes
genes = {}
with open(
    filename,  # pas de guillemet ici car filename est une variable
    "r",
) as file:
    for line in file:
        data = line.strip().split()
        chrom, start, stop, name = data[:4]
        if (
            chrom not in genes
        ):  # si la clé chrom n'existe pas dans le dictionnaire genes
            genes[chrom] = (
                {}
            )  # on crée une nouvelle clé chrom dans le dictionnaire genes
        genes[chrom][name] = (
            int(start),
            int(stop),
        )  # permet de convertir les valeurs en entier

pprint.pp(genes)

# local base => chemin relatif ::::

# script a executer dans le terminal

#  python TP_01/script/tp_dist.py TP_01/data/tf_400.bed
