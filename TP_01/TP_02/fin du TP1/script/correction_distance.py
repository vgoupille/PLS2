from pprint import pprint
import sys

#
# genes = {"chr12":
#             {"AREHF": (34564, 65432),
#              "FJHJR": (65434, 87654)
#             },
#           "chr3":
#             {"UTHF4": (124, 6542),
#              "VJFR8": (124552, 857389)
#             }
#          }
# print(genes["chr12"])


# Récupère le nom du fichier dans la ligne de commande
filename = sys.argv[1]
# Créer un dictionnaire vide pour stocker les positions des gènes
# genes = {}
# with open(filename, "r") as file:
#     for ligne in file:
#         data = ligne.strip().split()
#         chrom, start, stop, name = data[:4]
#         if chrom not in genes:
#             genes[chrom] = {}
#         genes[chrom][name] = (int(start), int(stop))


def read_bed(filename):
    """Lit un fichier bed et range les 4 premières colonnes"""
    dico = {}
    with open(filename, "r") as file:
        for ligne in file:
            data = ligne.strip().split()
            chrom, start, stop, name = data[:4]
            if chrom not in dico:
                dico[chrom] = {}
            dico[chrom][name] = (int(start), int(stop))
    return dico


def distance(start_g, stop_g, start_f, stop_f):
    if start_f > stop_g:
        return start_f - stop_g
    if start_g > stop_f:
        return start_g - stop_f
    return 0


genes = read_bed(sys.argv[1])
tfact = read_bed(sys.argv[2])

with open("result.csv", "w", encoding="utf-8") as file:
    for chrom, sub_gene in genes.items():
        if chrom in tfact:  # test si chrom est une clé de tfact
            sub_fact = tfact[chrom]
            for gene, (start_g, stop_g) in sub_gene.items():
                for fact, (start_f, stop_f) in sub_fact.items():
                    d = distance(start_g, stop_g, start_f, stop_f)
                    if d < 500000:
                        file.write(f"{chrom}\t{gene}\t{fact}\t{d}\n")
