import pandas as pd

# read the csv files
df = pd.read_csv('tblastn_summary_id80_cover80_cds_brainimmu_nonprimate.csv')
df2 = pd.read_csv('uniprot_normal_tissue_ABCtotal_reviewed_dedup.csv')

gene_list = []
for column_name in df.columns:
    match_row = df2[df2['Entry'] == column_name]
    #print(match_row)
    if not match_row.empty:
        gene_list.append(match_row['From'].values[0])
    else:
        gene_list.append(None)  # Append None if there's no match

df.loc[len(df)] = gene_list

# save the updated dataframe to a new csv file
df.to_csv('tblastn_summary_id80_cover80_cds_brainimmu_nonprimate_genes.csv', index=False)