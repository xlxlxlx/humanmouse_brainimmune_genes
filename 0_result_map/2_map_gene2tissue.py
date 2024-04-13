import pandas as pd


def process_dataframe(df_main, df_sub, df_result_name):
    """
    This function checks if values in the first row of df_main are in df_sub[column_name].
    If a match is found, it transposes the corresponding row from df_sub and appends
    it to df_main.

    Args:
    df_main (pd.DataFrame): The main DataFrame to append to.
    df_sub (pd.DataFrame): The reference DataFrame to check values from.
    file_name: The filename for the result to be saved to.
    """

    custom_index = list(df_main.index) + ['Gene', 'Gene name', 'Tissue', 'Cell type', 'Level', 'Reliability']
    df_result = pd.DataFrame(index=custom_index)

    df_first_row = df_main.iloc[0]

    for col in df_main.columns:
        if df_first_row[col] in df_sub['Gene name'].values:
            row_to_append = df_sub[df_sub['Gene name'] == df_first_row[col]].iloc[0].tolist()

            df_result[col] = df_main[col].tolist() + row_to_append

    # Save the result dataframe to a CSV file
    df_result.to_csv(f"{df_result_name}.csv", index=True, header=False)


# Read the CSV files
df = pd.read_csv('tblastn_summary_id80_cover80_cds_brainimmu_nonprimate_genes.csv', header=None, index_col=0)

df_x = pd.read_csv('normal_tissue_brain1.csv')
df_y = pd.read_csv('normal_tissue_brain2.csv')
df_z = pd.read_csv('normal_tissue_immu.csv')

# Combine df_y and df_z to handle duplicated rows
df_xy_combined = pd.concat([df_x, df_y]).drop_duplicates()
# Process combined df_y and df_z
process_dataframe(df, df_xy_combined, 'cds_brainimmu_nonprimate_genes_brain')

process_dataframe(df, df_z, 'cds_brainimmu_nonprimate_genes_immu')

