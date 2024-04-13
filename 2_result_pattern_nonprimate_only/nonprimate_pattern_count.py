import pandas as pd
import numpy as np
import itertools
from collections import Counter

tissue_list = ["brain", "immu", "BI"]

for tissue in tissue_list:

    fn = f'cds_brainimmu_nonprimate_genes_{tissue}_distribution'
    df2 = pd.read_csv(f'{fn}.csv', index_col=0)

    # Generate all 8 possible patterns of 4 bits (0s and 1s)
    patterns = list(itertools.product([0, 1], repeat=4))

    indices_nonprimate = ['Mus musculus','Canis lupus familiaris','Orycteropus afer afer','Danio rerio']

    # Dictionary to hold column names and their corresponding patterns
    col_patterns = {}

    for column in df2.columns:
        for pattern in patterns:
            pattern = list(pattern)
            pattern = [str(i) for i in pattern]
            if df2.loc[indices_nonprimate, column].tolist() == pattern:
                # Add the pattern as a key and column name as a value to the dictionary
                col_patterns[column] = "".join(map(str, pattern))


    # Sort df2 columns by the patterns
    df2 = df2[sorted(col_patterns, key=col_patterns.get)]
    df2.to_csv(f'{fn}_sorted.csv', index=True)

    # Create pattern-count table for df2
    pattern_counts = Counter(col_patterns.values())
    df_pattern_counts = pd.DataFrame.from_dict(pattern_counts, orient='index', columns=['Count'])
    df_pattern_counts.index.name = 'Pattern'

    # Save the pattern-count table to a CSV file
    df_pattern_counts.to_csv(f'{fn}_pattern_counts.csv')