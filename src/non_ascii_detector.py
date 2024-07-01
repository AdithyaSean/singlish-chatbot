import json

# Initialize an empty set to store unique Unicode numbers of non-ASCII characters
non_ascii_unicode_numbers = set()

# Open the reddit.jsonl file for reading
with open('datasets/singlish/reddit.jsonl', 'r', encoding='utf-8') as file:
    # Process each line in the file
    for line in file:
        # Parse the line as JSON
        data = json.loads(line)
        
        # Extract the input_text and output_text fields
        input_text = data.get('input_text', '')
        output_text = data.get('output_text', '')
        
        # Combine input_text and output_text for processing
        combined_text = input_text + output_text
        
        # Iterate through each character in the combined text
        for char in combined_text:
            # Check if the character is non-ASCII
            if ord(char) > 127:
                # Determine the format based on the Unicode number range
                if ord(char) < 0x10000:
                    # Format as \uXXXX for characters in the BMP
                    non_ascii_unicode_numbers.add(f'\\u{ord(char):04X}')
                else:
                    # Format as \UXXXXX for characters outside the BMP
                    non_ascii_unicode_numbers.add(f'\\U{ord(char):05X}')
    
    # Convert the set to a sorted list to display the Unicode representations in order
    sorted_non_ascii_unicode_numbers = sorted(list(non_ascii_unicode_numbers))
    
    # Create or open the output file in write mode
    with open('datasets/singlish/non_ascii_unicode_numbers.txt', 'w', encoding='utf-8') as output_file:
        # Write each Unicode representation to the file, each on a new line
        for unicode_representation in sorted_non_ascii_unicode_numbers:
            output_file.write(f'{unicode_representation}\n')
    
    # Optionally, print a message indicating completion
    print('Unicode representations in \\uXXXX format have been written to non_ascii_unicode_numbers.txt')