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


for chrom in genes:  # parcours les clefs du dictionnaire genes
    print(chrom)  # return la clef

for chrom in genes.keys():
    print(chrom)  # return la clef

for chrom in genes.values():
    print(chrom)  # return la valeur

for chrom, sub_gene in genes.items():
    print(chrom)  # return la valeur
    print(sub_gene)  # return la valeur


def distance(gene_start, gene_stop, tf_start, tf_stop):
    if gene_stop < tf_start:
        return tf_start - gene_stop
    if tf_stop < gene_start:
        return gene_start - tf_stop
    return 0


with open("output.txt", "w", encoding="utf-8") as file:
    for chrom, sub_gene in genes.items():
        if chrom in tfact:  # si la clef est dans le dictionnaire tfact
            sub_fact = tfact[chrom]  # alors on recupere la valeur de la clef
            for gene, (start_gene, stop_gene) in sub_gene.items():
                for fact, (start_fact, stop_fact) in sub_fact.items():
                    d = distance(start_gene, stop_gene, start_fact, stop_fact)
                    if d < 500000:
                        print(gene, fact, d, sep="\t")
                        file.write(f"{chrom}\t{gene}\t{fact}\t{d}\n")
