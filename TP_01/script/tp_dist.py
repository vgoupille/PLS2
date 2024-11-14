import sys
import pprint as pprint  # module pour afficher des données de manière plus lisible

filename = sys.argv[1]
# liste des arguments passés en ligne de commande (argv[0] est le nom du script), argv est une liste


# creation d'un dictionnaire pour stocker les positions des gènes
genes = {}
with open(
    "filename",
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

# python tp_dist.py TP_01/data/tf_400.bed
