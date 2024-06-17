import json

def sinhala_to_singlish(sinhala_word):
    """Transliterates a Sinhala word to Singlish."""

    # Base consonants and independent vowels
    sinhala_mapping = {
        'අ': 'a', 'ආ': 'aa', 'ඇ': 'a', 'ඈ': 'aa', 'ඉ': 'i', 'ඊ': 'ee', 'උ': 'u', 'ඌ': 'uu',
        'ඍ': 'ru', 'ඎ': 'ruu', 'ඏ': 'lu', 'ඐ': 'luu', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o',
        'ඕ': 'oo', 'ඖ': 'au',
        'ක': 'ka', 'ඛ': 'kha', 'ග': 'ga', 'ඝ': 'gha', 'ඞ': 'nga', 'ච': 'cha', 'ඡ': 'cha', 'ජ': 'ja',
        'ඣ': 'jha', 'ඤ': 'nya', 'ට': 'ta', 'ඨ': 'ta', 'ඩ': 'da', 'ඪ': 'da', 'ණ': 'na', 'ත': 'tha',
        'ථ': 'tha', 'ද': 'da', 'ධ': 'dha', 'න': 'na', 'ප': 'pa', 'ඵ': 'pa', 'බ': 'ba', 'භ': 'bha',
        'ම': 'ma', 'ය': 'ya', 'ර': 'ra', 'ල': 'la', 'ව': 'wa', 'ශ': 'sha', 'ෂ': 'sha', 'ස': 'sa',
        'හ': 'ha', 'ළ': 'la', 'ෆ': 'fa', 'ං': 'ng', 'ඃ': 'h',
        # ... (Add any other special characters or independent vowels)
    }

    # Vowel modifiers and their corresponding sounds
    vowel_modifiers = {
        '්': '', 'ා': 'a', 'ැ': 'a', 'ෑ': 'aa', 'ි': 'i', 'ී': 'ee', 'ු': 'u', 'ූ': 'oo',
        'ෙ': 'e', 'ේ': 'ee', 'ෛ': 'ai', 'ො': 'o', 'ෝ': 'oo', 'ෞ': 'au',
        'ෟ': 'ru', 'ෳ': 'ruu'
    }

    english_word = ""
    i = 0
    while i < len(sinhala_word):
        char = sinhala_word[i]

        # Check for consonant-vowel combinations
        if char in sinhala_mapping and i + 1 < len(sinhala_word):
            next_char = sinhala_word[i + 1]
            if next_char in vowel_modifiers:
                combined_char = char + next_char
                english_word += sinhala_mapping.get(combined_char, sinhala_mapping.get(char, '') + vowel_modifiers.get(next_char, ''))
                i += 2  # Skip the next character (vowel modifier)
                continue

        # Handle yansaya (්‍ය)
        if char == '්‍ය':
            prev_char = sinhala_word[i - 1]
            if prev_char in ['න්', 'ද', 'ධ']:
                english_word = english_word[:-1] + 'y' + sinhala_mapping.get(prev_char, '') + 'a'
                i += 1
                continue

        # Default case: transliterate individual character
        english_word += sinhala_mapping.get(char, char)
        i += 1

    return english_word

def transliterate_jsonl(input_file, output_file):
    """Transliterates Sinhala words in a JSONL file to Singlish."""

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            try:
                data = json.loads(line)
                if 'title' in data:
                    data['title'] = sinhala_to_singlish(data['title'])
                if 'text' in data:
                    data['text'] = sinhala_to_singlish(data['text'])
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

# Get input and output file paths
input_file = input("Enter the path to your Sinhala input JSONL file: ")
output_file = input("Enter the desired path for the Singlish output JSONL file: ")

transliterate_jsonl(input_file, output_file)
