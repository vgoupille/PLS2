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

print("Genes on chr12:")
pprint.pp(genes["chr12"])

print("\nTranscription factors on chr12:")
pprint.pp(tfact["chr12"])

# python TP_01/script/tp_dist_function.py  TP_01/data/gene_chr12.bed TP_01/data/tf_chr12.bed

""" example :
'TF_39464': (96125304, 96125798),
'TF_39465': (96183409, 96185403),
'TF_39466': (96251970, 96253573),
'TF_39467': (96312014, 96313121),
'TF_39468': (96336179, 96337565),
'TF_39469': (96357685, 96358989),
'TF_39470': (96392317, 96392943),"""
