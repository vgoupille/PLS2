import sys
import pandas as pd
import time

# Start the timer
start_time = time.time()


# foction pour calculer la distance entre deux genes
def distance(start_g, stop_g, start_f, stop_f):
    if start_f > stop_g:
        return start_f - stop_g
    if start_g > stop_f:
        return start_g - stop_f
    return 0


genes = pd.read_csv(sys.argv[1], sep="\t", header=None)
tfact = pd.read_csv(sys.argv[2], sep="\t", header=None)
# print(genes)
# print(tfactors)

dfg = genes.iloc[:, :4]  # select the first 4 columns and all the rows
dft = tfact[[0, 1, 2, 3]]  # select the first 4 columns and all the rows

# iloc [rows, columns] # acces par index
# loc[] access par vrai/FAUX  sur les lignes
# [] = acces par colonnes

# # add column names
dfg.columns = ["chr", "startg", "stopg", "gene"]
dft.columns = ["chr", "startt", "stopt", "tf"]


for g_index in range(len(dfg["chr"])):
    chrom = dfg.iloc[g_index, 0]
    start_gene = dfg.iloc[g_index, 1]
    stop_gene = dfg.iloc[g_index, 2]
    gene = dfg.iloc[g_index, 3]
    my_filter = dft["chr"] == chrom
    sub_dft = dft.loc[filter]
    print(sub_dft)
    print(chrom)
    break  # arret du programme sur la premiere iteration


for f_index in range(len(sub_dfg["chr"])):
    chrom = dfg.iloc[g_index, 0]
    start_f = dfg.iloc[g_index, 1]
    stop_f = dfg.iloc[g_index, 2]
    gene = dfg.iloc[g_index, 3]
    my_filter = dft["chr"] == chrom
    sub_dft = dft.loc[filter]
    print(sub_dft)
    print(chrom)
    break  # arret du programme sur la premiere iteration


# End the timer
end_time = time.time()

# Calculate and print the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")

# python "TP_01/TP_02/fin du TP1/script/TP_panda_gene_tf.py" TP_01/data/gene_300.bed TP_01/data/tf_400.bed
