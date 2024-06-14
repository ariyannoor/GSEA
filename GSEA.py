import pandas as pd
import gseapy as gp

# Paths to your .gct and .gmt files 
gct_file = '/Users/ariyan/Desktop/GSEA using logfold chang/pam3cys-RNA-with-common.gct'
gmt_file = '/Users/ariyan/Desktop/GSEA using logfold chang/mir351_targets_cleaned2.gmt'

# Read the data
data = pd.read_csv(gct_file, sep='\t', skiprows=2, index_col=0)

# Run GSEA
ssgsea_results = gp.ssgsea(data=data, 
                           gene_sets=gmt_file, 
                           outdir='ssgsea_output', 
                           min_size=3, 
                           max_size=5000, 
                           permutation_num=1000, 
                           no_plot=True)

# View the results
print(ssgsea_results.res2d.head())