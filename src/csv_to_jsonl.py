import pandas as pd
import json

def csv_to_jsonl(csv_file, jsonl_file):
    """Converts a CSV file to JSONL format.

    Args:
        csv_file (str): Path to the input CSV file.
        jsonl_file (str): Path to the output JSONL file.
    """

    df = pd.read_csv(csv_file)  # Read the entire CSV into a DataFrame

    with open(jsonl_file, 'w', encoding='utf-8') as f:
        for index, row in df.iterrows():
            data = row.to_dict()  # Convert each row to a dictionary
            f.write(json.dumps(data, ensure_ascii=False) + '\n')  # Write each dictionary as a JSON object on a new line

# Get input and output file paths from the user
csv_file = input("Enter the path to your CSV file: ")
jsonl_file = input("Enter the desired path for the JSONL file: ")

csv_to_jsonl(csv_file, jsonl_file)

print(f"CSV file converted to JSONL and saved to: {jsonl_file}")
