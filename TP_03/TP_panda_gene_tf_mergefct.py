import sys
import pandas as pd
import time

# Start the timer
start_time = time.time()


# Function to calculate the distance between two genes
def distance(start_g, stop_g, start_f, stop_f):
    if start_f > stop_g:
        return start_f - stop_g
    if start_g > stop_f:
        return start_g - stop_f
    return 0


if __name__ == "__main__":
    # Load files
    genes = pd.read_csv(sys.argv[1], sep="\t", header=None)
    tfact = pd.read_csv(sys.argv[2], sep="\t", header=None)

    # Select the first columns and assign names
    dfg = genes.iloc[:, :4]
    dft = tfact.iloc[:, :4]

    dfg.columns = ["chr", "startg", "stopg", "gene"]
    dft.columns = ["chr", "startt", "stopt", "tf"]

    # Group by chromosome
    group_gene = dfg.groupby("chr")
    group_ft = dft.groupby("chr")

    # Result list to store calculated distances
    results = []

    with open("TP_03/resultsmerge.csv", "w", encoding="utf-8") as output_file:
        for chrom, sub_gene in group_gene:
            if chrom in group_ft.groups:
                sub_ft = group_ft.get_group(chrom)
                for _, (_, start_gene, stop_gene, gene) in sub_gene.iterrows():
                    for _, (_, start_tf, stop_tf, tf) in sub_ft.iterrows():
                        d = distance(start_gene, stop_gene, start_tf, stop_tf)
                        if d < 500000:
                            output_file.write(f"{gene},{tf},{chrom},{d}\n")

    # Print the elapsed time
    print(f"Elapsed time: {time.time() - start_time} seconds")

    # python "TP_03/TP_panda_gene_tf_mergefct.py" TP_01/TP_dist_gene_TF/data/gene_300.bed TP_01/TP_dist_gene_TF/data/tf_400.bed

    # cs50 havard
