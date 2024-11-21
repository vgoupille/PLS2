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

genes = read_bed(sys.argv[1])
tfact = read_bed(sys.argv[2])
pprint(genes["chrX"])
pprint(tfact["chrX"])