import pandas as pd

# Define the path to your TSV file
tsv_file = 'datasets-sinhala/semiSOLD.tsv'

# Read the TSV file into a pandas DataFrame
df = pd.read_csv(tsv_file, sep='\t')

# Define the output CSV file path
csv_file = 'datasets-sinhala/semiSOLD.csv'

# Write the DataFrame to a CSV file
df.to_csv(csv_file, index=False)

print(f'Conversion completed. CSV file saved to {csv_file}')
