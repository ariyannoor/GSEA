# Import the pandas library
import pandas as pd
# Define the path to the GCT file
gct_file_path = '/Users/ariyan/Desktop/EAE-RNA.gct'
# Read the GCT file
with open (gct_file_path) as f:
    # read data as data frame 
    df = pd.read_csv(f, sep='\t')
    # print the data frame
print (df.head())

# Define path for the output CSV file 
csv_file_path = '/Users/ariyan/Desktop/EAE-RNA.csv'

# Save the data frame to a CSV file
df.to_csv(csv_file_path, index=False)
# print the path of the output CSV file
print("CSV file saved at: ", csv_file_path)
