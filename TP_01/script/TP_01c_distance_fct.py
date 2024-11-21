# Exercice pour calculer les distances entre les gènes et les facteurs de transcription sur un genes


# Si recouvrement ou inclusion alors distance = 0

# objectif :
# calculer la distance entre les gènes et les facteurs de transcription
# creation d'une fonction distance_gene_tf


def distance_gene_tf(start_gene, stop_gene, start_tf, stop_tf):
    if (start_tf <= stop_gene and stop_tf >= start_gene) or (
        start_gene <= stop_tf and stop_gene >= start_tf
    ):  # le cas ou il y a inclusion du gène dans le facteur de transcription ou du facteur de transcription dans le gène ou bien recouvrement
        return 0  ## distance = 0
    elif (
        start_tf > stop_gene
    ):  # le cas ou le facteur de transcription est après le gène
        return start_tf - stop_gene  ## distance = start_tf - stop_gene
    else:  # le cas ou le facteur de transcription est avant le gène
        return start_gene - stop_tf  ## distance = start_gene - stop_tf


def distance_gene_tf2(start_gene, stop_gene, start_tf, stop_tf):
    res = 0
    if stop_gene < start_tf:
        res = start_tf - stop_gene
    elif stop_tf < start_gene:
        res = start_gene - stop_tf
    return res


def distance_gene_tf3(start_gene, stop_gene, start_tf, stop_tf):
    if stop_gene < start_tf:
        return start_tf - stop_gene
    if stop_tf < start_gene:
        return start_gene - stop_tf
    return 0
