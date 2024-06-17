import pandas as pd

parquet_file = input("Enter the path to the parquet file: ")

jsonl_file = input("Enter the path to the output JSONL file: ")

df = pd.read_parquet(parquet_file)

df.to_json(jsonl_file, orient='records', lines=True)
