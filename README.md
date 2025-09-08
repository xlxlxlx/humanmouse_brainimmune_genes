# Comparative Genomics of Human Brain and Immune Gene Conservation Across Species

This is a repository storing data and scripts used in our manuscript titled "Comparative Genomics of Human Brain and Immune Gene Conservation Across Species".

## Data files
- genome_accession.xlsx    
The genome accession numbers for the 32 primate genomes and 4 non-primate species used in this study, obtained form Ensembl [^2] and NCBI [^3].

- uniprot_normal_tissue_ABCtotal_reviewed_dedup  
The 1389 brain or immune system highly expressed genes analyzed in the paper, with at least one "reviewed" protein and deduped by keeping the first valid entry in UniProt mapping results [^1]. 

- uniprot_random304_reviewed_dedup.csv   
A random set of 304 human genes and their corresponding proteins used in this study.

- uniprot_mousebrain_top100genes_reviewed_dedup.csv   
The mouse genes with top 100 nTPM values and their corresponding proteins used in this study.   

- Homo_sapiens_GRCh38_cds_list.csv   
The full human gene list extracted from human CDS sequence obtained from Ensembl [^3]. Note there are duplicated gene names.

- fasta2genelist.py    
The script used to extract the full human gene list from human CDS sequence file.


## Scripts
The scripts are labeled according to their order of execution. If two scripts share the same preceeding number, this indicates that there is no strict sequence for executing them.

### blast_alignment
Scripts and files under this folder are for human gene alignment to primate and nonprimate coding sequences.

- 1_tblastn_protein_cds.py   
Align protein sequence to CDS sequence   

- 2_tblastn_result2sql.py   
Input the aligning results into a relational database

- 3_tblastn_summary_thre_cgc_nonprimate.py   
Summarize the aligning result into a gene x species matrix   

- protein_primate_brainimmu_thre80.sql, protein_nonprimate_brainimmu_thre80.sql   
The database table creation files when a new database table is needed   

### 0_result_filter_map
Inputs are outputs from blast_alignment. The scripts map proteins to genes and to different subsets (B, I, and C as indicated in the paper).   

- 1_protein2gene_name.py   
Map proteins to their gene names and filter results by a given gene list.   

- 2_map_gene2tissue.py   
Map genes to their highly expressed tissue(s).   

- 3_overlap_filter_BI.py   
Identify intersection of genes highly expressed in brain and in the immune system (set C in the paper).   

### 1_result_distribution
Inputs are outputs from 0_result_filter_map. The script generates the binary distribution of genes across species.   

- values_to_binary.py   
Map values to 0 or 1, then seperate the results into tables containing all 1s, all 0s, and the remaining.   


### 2_result_pattern_nonprimate_only
Inputs are outputs from 1_result_distribution. The scripts count the number of each nonprimate pattern within a given data set.   

- nonprimate_pattern_count.py   
Count the number of each nonprimate pattern in the entire cancer gene set.    

### 2_result_PandNP
Inputs are outputs from 1_result_distribution. The script combines primate gene distribution results with nonprimate patterns.   

- primate_nonprimate_matching.py   
Generate nonprimate patterns based on gene binary distribution across nonprimate species. Then combines the nonprimate patterns with the gene distribution across primate species.    

### 3_result_clades
Inputs are outputs from 1_result_distribution. The script combines primate gene distribution results with nonprimate patterns.   

- 1_clade_assigner.py   
Identify genes that are absent from an entire primate clade.   

- 2_clades_pattern_filter_<set>.py   
Categorize clade assigning results to each set (B, I, and C). 

### 4_result_tissue_count
Inputs are outputs 3_result_clades. Scripts under this folder counts the number of tissues each gene is highly expressed in, given a list of genes.   

- 1_gene_tissue_count.py    
Count number of tissues each gene is highly expressed in, given CSV files.   

- 2_df_list_count.py   
Count number of tissues each gene is highly expressed in, given CSV files containing genes absent from primate clades.   

- 2_basic_mean_mode
A simple script to caculate and print statistical metrics for a given number list.   



[^1]: "UniProt: the universal protein knowledgebase in 2023." Nucleic Acids Research 51, no. D1 (2023): D523-D531.
[^2]: Cunningham, Fiona, et al. "Ensembl 2022." Nucleic acids research 50.D1 (2022): D988-D995.
[^3]: Sayers, Eric W., et al. "Database resources of the national center for biotechnology information." Nucleic acids research 50.D1 (2022): D20.


