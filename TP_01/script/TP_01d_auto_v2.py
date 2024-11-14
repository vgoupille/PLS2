import random
import sys  # module for reading command line arguments
import pprint as pprint  # module for pretty printing data


def read_bed(filename):
    """Reads a BED file and returns a dictionary with gene positions."""
    dico = {}
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split()
            chrom, start, stop, name = data[:4]
            if chrom not in dico:
                dico[chrom] = {}
            dico[chrom][name] = (int(start), int(stop))
    return dico


def distance_gene_tf(start_gene, stop_gene, start_tf, stop_tf):
    """Calculates the distance between a gene and a transcription factor."""
    if (start_tf <= stop_gene and stop_tf >= start_gene) or (
        start_gene <= stop_tf and stop_gene >= start_tf
    ):  # Case of overlap or inclusion
        return 0  # Distance = 0 (overlap or inclusion)
    elif start_tf > stop_gene:  # Transcription factor is after the gene
        return start_tf - stop_gene  # Distance = start_tf - stop_gene
    else:  # Transcription factor is before the gene
        return start_gene - stop_tf  # Distance = start_gene - stop_tf


def calculate_distances(genes, tfact, chrom):
    """Calculates the distances between genes and transcription factors for a specific chromosome."""
    distances = {}
    for gene_name, (start_gene, stop_gene) in genes.get(chrom, {}).items():
        for tf_name, (start_tf, stop_tf) in tfact.get(chrom, {}).items():
            # Calculate the distance between the gene and the transcription factor
            distance = distance_gene_tf(start_gene, stop_gene, start_tf, stop_tf)
            distances[(gene_name, tf_name)] = distance
    return distances


# Reading BED files
genes = read_bed(sys.argv[1])  # Gene file passed as first argument
tfact = read_bed(sys.argv[2])  # Transcription factor file passed as second argument

# Get the number of random genes and TFs from command-line arguments, with defaults
num_genes = int(sys.argv[3]) if len(sys.argv) > 3 else 10  # Default is 10
num_tfacts = int(sys.argv[4]) if len(sys.argv) > 4 else 10  # Default is 10

# Specify the chromosome you want to analyze (example: chr12)
chromosome = "chr12"

# Select random genes and transcription factors from the specified chromosome
random_genes = random.sample(
    list(genes[chromosome].keys()), min(num_genes, len(genes[chromosome]))
)
random_tfacts = random.sample(
    list(tfact[chromosome].keys()), min(num_tfacts, len(tfact[chromosome]))
)

# Create shorter dictionaries for selected genes and transcription factors, preserving the chromosome structure
selected_genes = {
    chromosome: {gene_name: genes[chromosome][gene_name] for gene_name in random_genes}
}
selected_tfacts = {
    chromosome: {tf_name: tfact[chromosome][tf_name] for tf_name in random_tfacts}
}
print(f"{num_genes} selected genes {chromosome}:")
pprint.pprint(selected_genes)
print(f"{num_tfacts} selected TF {chromosome}:")
pprint.pprint(selected_tfacts)

# Calculate the distances between the selected genes and transcription factors on the given chromosome
distances = calculate_distances(selected_genes, selected_tfacts, chromosome)

# Print the results for the selected genes and transcription factors
print(f"Distances between selected genes and transcription factors on {chromosome}:")
pprint.pprint(distances)

# python TP_01/script/TP_01d_auto_V2.py TP_01/data/gene_chr12.bed TP_01/data/tf_chr12.bed 15 20
