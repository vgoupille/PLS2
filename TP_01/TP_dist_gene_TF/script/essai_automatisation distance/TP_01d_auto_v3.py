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

# Get the chromosome to analyze from command-line arguments (default is "chr12")
chromosome = sys.argv[5] if len(sys.argv) > 5 else "chr12"  # Default is "chr12"

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

print(f"{num_genes} selected genes on {chromosome}:")
pprint.pprint(selected_genes)
print(f"{num_tfacts} selected TFs on {chromosome}:")
pprint.pprint(selected_tfacts)

# Calculate the distances between the selected genes and transcription factors on the given chromosome
distances = calculate_distances(selected_genes, selected_tfacts, chromosome)

# Print the results for the selected genes and transcription factors
print(f"Distances between selected genes and transcription factors on {chromosome}:")
pprint.pprint(distances)

# python TP_01/script/TP_01d_auto_V3.py TP_01/data/gene_chr12.bed TP_01/data/tf_chr12.bed 15 20 chr1

"""2 selected genes on chr12:
{'chr12': {'AICDA': (8754761, 8765442), 'MIR6505': (48526580, 48526650)}}
3 selected TFs on chr12:
{'chr12': 
    {'TF_38337': (46780746, 46782664),
    'TF_38512': (50580959, 50581590),
    'TF_40299': (124139528, 124140274)}}
Distances between selected genes and transcription factors on chr12:
{('AICDA', 'TF_38337'): 38015304,
('AICDA', 'TF_38512'): 41815517,
('AICDA', 'TF_40299'): 115374086,
('MIR6505', 'TF_38337'): 1743916,
('MIR6505', 'TF_38512'): 2054309,
('MIR6505', 'TF_40299'): 75612878}"""
