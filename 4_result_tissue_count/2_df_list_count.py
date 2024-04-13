import pandas as pd
import ast

tissue_list = ["brain", "immu","BI"]
clades_list = ["large", "small"]

for tissue in tissue_list:
    for clade in clades_list:

        file_name = f'{tissue}_proper_set_patterns_filtered_{clade}_{clade}clade_tissue.csv'
        df = pd.read_csv(file_name)

        def count_elements(list_str):
            try:
                lst = ast.literal_eval(list_str)
                return len(lst) if isinstance(lst, list) else 0
            except:
                return 0

        df['element_count'] = df.iloc[:, 1].apply(count_elements)

        new_file_name = file_name.rsplit('.', 1)[0] + '_count.csv'
        df.to_csv(new_file_name, index=False)

