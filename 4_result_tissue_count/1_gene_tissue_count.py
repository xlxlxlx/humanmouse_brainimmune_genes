import pandas as pd
tissue_list = ["brain", "immu","BI"]
clades_list = ["large", "small"]

for tissue in tissue_list:
    for clade in clades_list:

        fn = f'{tissue}_proper_set_patterns_filtered_{clade}'
        gene_csv = pd.read_csv(f'{fn}.csv', header=None)
        list_gene = gene_csv.iloc[33].tolist()

        df = pd.read_csv('normal_tissue.tsv', delimiter='\t')

        dict_rst = {}
        for gene in list_gene:
            filtered_df = df[(df['Gene name'] == gene) & (df['Level'] == 'High') & (df['Reliability'] == 'Enhanced')]
            list_tissue = list(set(filtered_df['Tissue']))
            dict_rst[gene] = list_tissue

        result_df = pd.DataFrame(list(dict_rst.items()), columns=['Gene', 'Tissue'])
        result_df.to_csv(f'{fn}_{clade}clade_tissue.csv', index=False)
