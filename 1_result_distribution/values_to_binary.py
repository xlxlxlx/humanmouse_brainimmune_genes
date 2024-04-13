import pandas as pd

indices_nonprimate = ['Mus musculus', 'Canis lupus familiaris', 'Orycteropus afer afer', 'Danio rerio']
indices_primate = ['Saimiri boliviensis boliviensis', 'Theropithecus gelada', 'Aotus nancymaae', 'Callithrix jacchus',
                   'Carlito syrichta', 'Cebus capucinus', 'Cercocebus atys', 'Chlorocebus sabaeus',
                   'Colobus angolensis palliatus', 'Gorilla gorilla', 'Homo sapiens', 'Macaca fascicularis',
                   'Macaca mulatta', 'Macaca nemestrina', 'Mandrillus leucophaeus', 'Microcebus murinus',
                   'Nomascus leucogenys', 'Otolemur garnettii', 'Pan paniscus', 'Pan troglodytes', 'Papio anubis',
                   'Piliocolobus tephrosceles', 'Pongo abelii', 'Prolemur simus', 'Propithecus coquereli',
                   'Rhinopithecus bieti', 'Rhinopithecus roxellana', 'Cebus imitator', 'Hylobates moloch',
                   'Lemur catta', 'Sapajus apella', 'Trachypithecus francoisi']

tissue_list = ["brain", "immu", "BI"]
species_list = ["primate", "nonprimate"]

for tissue in tissue_list:
    for species in species_list:
        filename = f"cds_brainimmu_{species}_genes_{tissue}"

        df = pd.read_csv(filename+".csv", index_col=0)
        df_new = df.copy()

        indices_to_modify = eval(f"indices_{species}")

        df_new.loc[indices_to_modify] = df_new.loc[indices_to_modify].applymap(
            lambda x: '0' if x in [' ', ''] or pd.isna(x) else '1')

        df_new.to_csv(filename+"_distribution.csv", index=True)

        # Select all the columns with all 1s
        df_ones = df_new.loc[:, (df_new.loc[indices_to_modify] == '1').all()]
        df_ones.to_csv(filename+'_all_ones.csv', index=True)

        # Select all the columns with all 0s
        df_zeros = df_new.loc[:, (df_new.loc[indices_to_modify] == '0').all()]
        df_zeros.to_csv(filename+'_all_zeros.csv', index=True)

        df_cols = set(df.columns)
        df_ones_cols = set(df_ones.columns)
        df_zeros_cols = set(df_zeros.columns)

        # Find the columns in df that are not in df_ones or df_zeros
        remaining_cols = df_cols - (df_ones_cols.union(df_zeros_cols))
        df_remaining = df_new[remaining_cols]
        df_remaining.to_csv(filename+'_proper_subset.csv', index=True)
