import json
import re

def remove_patterns(input_file, output_file):
    """Removes Reddit-style comment patterns and URL patterns from a JSONL file.

    Args:
        input_file (str): Path to the input JSONL file.
        output_file (str): Path to the output JSONL file.
    """

    comment_pattern = re.compile(r"^\*\s*(.*?)\s*/u/[\w,\s]+(?:\d+)?\*$")
    url_pattern = re.compile(r"_URL_\d+_")  # Pattern to match _URL_ followed by numbers and _

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            try:
                data = json.loads(line)
                if 'text' in data:
                    # Remove Reddit comment patterns
                    data['text'] = comment_pattern.sub(r"\1", data['text'])
                    # Remove URL patterns
                    data['text'] = url_pattern.sub("", data['text']) 
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line}")

# Get input and output file paths from the user
input_file = input("Enter the path to your JSONL file: ")
output_file = input("Enter the desired output file path: ")

remove_patterns(input_file, output_file)
