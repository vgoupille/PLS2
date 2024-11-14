import sys  # module pour lire les arguments passés en ligne de commande
import pprint as pprint  # module pour afficher des données de manière plus lisible


def read_bed(filename):
    """lit un fichier bed et retourne un dictionnaire avec les positions des gènes"""
    dico = {}
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split()
            chrom, start, stop, name = data[:4]
            if chrom not in dico:
                dico[chrom] = {}
            dico[chrom][name] = (int(start), int(stop))
    return dico


genes = read_bed(sys.argv[1])
tfact = read_bed(sys.argv[2])

pprint.pp(genes["chr12"])
pprint.pp(tfact["chr12"])

# python TP_01/script/tp_dist_function.py  TP_01/data/gene_chr12.bed TP_01/data/tf_chr12.bed
