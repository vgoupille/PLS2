import sys
import pandas as pd
import time

# Start the timer
start_time = time.time()


# Fonction pour calculer la distance entre deux gènes
def distance(start_g, stop_g, start_f, stop_f):
    if start_f > stop_g:
        return start_f - stop_g
    if start_g > stop_f:
        return start_g - stop_f
    return 0


# Chargement des fichiers
genes = pd.read_csv(sys.argv[1], sep="\t", header=None)
tfact = pd.read_csv(sys.argv[2], sep="\t", header=None)

# Sélection des premières colonnes et attribution des noms
dfg = genes.iloc[:, :4]
dft = tfact.iloc[:, :4]

dfg.columns = ["chr", "startg", "stopg", "gene"]
dft.columns = ["chr", "startt", "stopt", "tf"]

# Résultat final pour stocker les distances calculées
results = []

# Parcours des gènes
for g_index in range(len(dfg)):
    chrom = dfg.iloc[g_index]["chr"]
    start_gene = dfg.iloc[g_index]["startg"]
    stop_gene = dfg.iloc[g_index]["stopg"]
    gene = dfg.iloc[g_index]["gene"]

    # Filtrer les facteurs de transcription dans le même chromosome
    sub_dft = dft[dft["chr"] == chrom]

    # Calcul des distances pour chaque facteur de transcription
    for t_index in range(len(sub_dft)):
        start_tf = sub_dft.iloc[t_index]["startt"]
        stop_tf = sub_dft.iloc[t_index]["stopt"]
        tf = sub_dft.iloc[t_index]["tf"]

        # Calculer la distance
        d = distance(start_gene, stop_gene, start_tf, stop_tf)

        # Appliquer la condition de distance maximale
        if d < 500000:
            # Ajouter au résultat si la distance est inférieure à 500 000
            results.append([gene, tf, chrom, d])


# Convertir les résultats en DataFrame
results_df = pd.DataFrame(results, columns=["Gene", "TF", "Chromosome", "Distance"])

# Afficher les résultats
print(results_df)

# Fin du timer
end_time = time.time()

# Temps d'exécution
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")


# Exporter les résultats en fichier CSV
output_file = "results.csv"
results_df.to_csv(output_file, index=False)


# Ligne de commande pour exécuter le script a mettre dans le terminal
# python "TP_01/TP_02/fin du TP1/script/TP_panda_gene_tf.py" TP_01/data/gene_300.bed TP_01/data/tf_400.bed


# n'est pas vraiment optimal car on parcourt ligne par ligne  donc l'algo est long
# panda prefere column par column
