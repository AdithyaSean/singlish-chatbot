import json

def remove_url_column(input_file, output_file):
    """Removes the 'url' column from a JSONL file.

    Args:
        input_file (str): Path to the input JSONL file.
        output_file (str): Path to save the modified JSONL file.
    """

    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            data = json.loads(line)
            del data['english_question']
            del data['english_answer']
            del data['url']
            json.dump(data, outfile, ensure_ascii=False)
            outfile.write('\n')  # Add newline after each JSON object


# Get input and output file paths from the user
input_file = input("Enter the path to the JSONL file: ")
output_file = input("Enter the desired path for the new JSONL file: ")

remove_url_column(input_file, output_file)

print(f"The 'url' column has been removed. New file saved to: {output_file}")
