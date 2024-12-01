"""
    calculate distance with pandas
"""

import sys
import pandas as pd


def distance(start_g, stop_g, start_f, stop_f):
    """
    Calculate distance given start and stop positions
    of a gene and a trans factor
    """
    if start_f > stop_g:
        return start_f - stop_g
    if start_g > stop_f:
        return start_g - stop_f
    return 0


# def distance(row):
#     _, start_g, stop_g, _, start_f, stop_f, _ = row
#     if start_f > stop_g:
#         return start_f - stop_g
#     if start_g > stop_f:
#         return start_g - stop_f
#     return 0


if __name__ == "__main__":
    genes = pd.read_csv(sys.argv[1], sep="\t")
    tfact = pd.read_csv(sys.argv[2], sep="\t")

    dfg = genes.iloc[:, :4]
    dft = tfact.iloc[:, :4]

    dfg.columns = ["chr", "start_g", "stop_g", "gene"]
    dft.columns = ["chr", "start_f", "stop_f", "fact"]

    group_genes = dfg.groupby(by="chr")
    group_facts = dft.groupby(by="chr")

    # stock = []
    # for chrom, sub_gene in group_genes:
    #     if chrom in group_facts.groups:
    #         sub_fact = group_facts.get_group(chrom)
    #         df_full = pd.merge(sub_gene, sub_fact, how="left", on="chr")
    #         df_full["dist"] = 0
    #         filter1 = df_full["start_g"] > df_full["stop_f"]
    #         df_full.loc[filter1, "dist"] = df_full["start_g"] - df_full["stop_f"]
    #         filter2 = df_full["start_f"] > df_full["stop_g"]
    #         df_full.loc[filter2, "dist"] = df_full["start_f"] - df_full["stop_g"]
    #         df_full = df_full[df_full["dist"] < 500000]
    #         df_full = df_full[["chr", "gene", "fact", "dist"]]
    #         stock.append(df_full)
    # full = pd.concat(stock)
    # full.to_csv("result7.csv", index=False, sep='\t')

    # stock = []
    # for chrom, sub_gene in group_genes:
    #     if chrom in group_facts.groups:
    #         sub_fact = group_facts.get_group(chrom)
    #         df_full = pd.merge(sub_gene, sub_fact, how="left", on="chr")
    #         df_full["dist"] = df_full.apply(distance, axis=1)
    #         df_full = df_full[df_full["dist"] < 500000]
    #         df_full = df_full[["chr", "gene", "fact", "dist"]]
    #         stock.append(df_full)
    # full = pd.concat(stock)
    # full.to_csv("result6.csv", index=False, sep='\t')

    # with open("result5.csv", "w", encoding="utf-8") as output_file:
    #     for chrom, sub_gene in group_genes:
    #         if chrom in group_facts.groups:
    #             sub_fact = group_facts.get_group(chrom)
    #             df_full = pd.merge(sub_gene, sub_fact, how="left", on="chr")
    #             df_full["dist"] = df_full.apply(distance, axis=1)
    #             df_full = df_full[df_full["dist"] < 500000]
    #             for _, row in df_full.iterrows():
    #                 output_file.write(f"{chrom}\t{row['gene']}\t{row['fact']}\t{row['dist']}\n")

    # with open("result4.csv", "w", encoding="utf-8") as output_file:
    #     for chrom, sub_gene in group_genes:
    #         if chrom in group_facts.groups:
    #             sub_fact = group_facts.get_group(chrom)
    #             df_full = pd.merge(sub_gene, sub_fact, how="left", on="chr")
    #             for _, row in df_full.iterrows():
    #                 d = distance(row)
    #                 if d < 500000:
    #                     output_file.write(f"{chrom}\t{row['gene']}\t{row['fact']}\t{d}\n")

    # with open("result3.csv", "w", encoding="utf-8") as output_file:
    #     for chrom, sub_gene in group_genes:
    #         if chrom in group_facts.groups:
    #             sub_fact = group_facts.get_group(chrom)
    #             for _, (_, start_gene, stop_gene, gene) in sub_gene.iterrows():
    #                 for _, (_, start_fact, stop_fact, fact) in sub_fact.iterrows():
    #                     d = distance(start_gene, stop_gene, start_fact, stop_fact)
    #                     if d < 500000:
    #                         output_file.write(f"{chrom}\t{gene}\t{fact}\t{d}\n")

    with open("result2.csv", "w", encoding="utf-8") as file:
        for g_index in range(len(dfg["chr"])):
            chrom = dfg.iloc[g_index, 0]
            start_gene = dfg.iloc[g_index, 1]
            stop_gene = dfg.iloc[g_index, 2]
            gene = dfg.iloc[g_index, 3]
            myfilter = dft["chr"] == chrom
            sub_dft = dft.loc[myfilter]
            for f_index in range(len(sub_dft["chr"])):
                start_fact = sub_dft.iloc[f_index, 1]
                stop_fact = sub_dft.iloc[f_index, 2]
                fact = sub_dft.iloc[f_index, 3]
                d = distance(start_gene, stop_gene, start_fact, stop_fact)
                if d < 500000:
                    file.write(f"{chrom}\t{gene}\t{fact}\t{d}\n")
