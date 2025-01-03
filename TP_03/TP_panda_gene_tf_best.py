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

    # Merge dataframes on chromosome
    merged_df = pd.merge(dfg, dft, on="chr", suffixes=("_gene", "_tf"))

    # Calculate distances and filter
    merged_df["distance"] = merged_df.apply(
        lambda row: distance(row["startg"], row["stopg"], row["startt"], row["stopt"]),
        axis=1,
    )
    filtered_df = merged_df[merged_df["distance"] < 500000]

    # Write results to file
    filtered_df[["gene", "tf", "chr", "distance"]].to_csv(
        "results.csv", index=False, header=False
    )

    # Print the elapsed time
    print(f"Elapsed time: {time.time() - start_time} seconds")
