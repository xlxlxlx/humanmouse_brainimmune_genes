import pandas as pd
import numpy as np
import itertools
from collections import Counter

tissue_list = ["brain", "immu", "BI"]
dist_list = ['all_zeros', "proper_subset", "all_ones"]

for tissue in tissue_list:
    for dist in dist_list:

        fn = f'cds_brainimmu_primate_genes_{tissue}_{dist}'

        df1, df2 = pd.read_csv(f'input/{fn}.csv', index_col=0, header=1), pd.read_csv(
            'input/tblastn_summary_id80_cover80_cds_brainimmu_nonprimate_distribution.csv')

        # Generate all 8 possible patterns of 4 bits (0s and 1s)
        patterns = list(itertools.product([0, 1], repeat=4))

        # Prepare an empty DataFrame
        df_new = pd.DataFrame()

        for column in df1.columns:
            for pattern in patterns:
                pattern = list(pattern)
                if df2[column].tolist() == pattern:
                    # Append the pattern as a row to the column
                    df_new[column] = df1[column].tolist() + ["'" + "".join(map(str, pattern)) + "'"]

        df_new.index = list(df1.index) + ['non_primates']

        # Convert the pattern row to the object type to keep leading zeros
        df_new.loc["non_primates"] = df_new.loc["non_primates"].astype(str)

        # Sort columns by the pattern row (last row)
        df_new = df_new.reindex(sorted(df_new.columns, key=lambda x: df_new[x].iloc[-1]), axis=1)

        # Save the DataFrame to a new CSV file
        df_new.to_csv(f'{fn}_with_patterns.csv', index=True)
