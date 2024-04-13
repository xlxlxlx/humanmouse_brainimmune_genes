import pandas as pd


def filter_and_save_csv(input_csv, output_csv, list_x):
    df = pd.read_csv(input_csv, index_col=0)
    columns_to_keep = [col for col in df.columns if df.at["Gene name", col] in list_x]

    filtered_df = df[columns_to_keep]

    filtered_df.to_csv(output_csv, index=False)


list_largeclades = []
filter_and_save_csv('cds_brainimmu_primate_genes_brain_proper_subset_with_patterns.csv',
                    'brain_proper_set_patterns_filtered_large.csv', list_largeclades)
list_smallclades = []
filter_and_save_csv('cds_brainimmu_primate_genes_brain_proper_subset_with_patterns.csv',
                    'brain_proper_set_patterns_filtered_small.csv', list_smallclades)
