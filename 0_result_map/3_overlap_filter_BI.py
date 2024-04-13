import pandas as pd

# Function to save the overlapping columns of two dataframes to a new CSV file
def save_overlapping_columns(df1, df2, result_file_name):
    # Identify the overlapping columns
    overlapping_columns = df1.columns.intersection(df2.columns)

    # Create a new dataframe with only the overlapping columns
    df_result = pd.DataFrame()
    for col in overlapping_columns:
        df_result[col] = df1[col]

    # Save the result dataframe to a CSV file
    df_result.to_csv(f"{result_file_name}.csv", index=False, header=True)

# Load the dataframes from their respective CSV files
df_x_result = pd.read_csv('cds_brainimmu_nonprimate_genes_brain.csv')
df_yz_result = pd.read_csv('cds_brainimmu_nonprimate_genes_immu.csv')

# Save the overlapping columns to a new CSV file
save_overlapping_columns(df_x_result, df_yz_result, 'cds_brainimmu_nonprimate_genes_BI')