import json

def sinhala_to_singlish(sinhala_text):
    vowels = {'අ': 'a', 'ආ': 'aa', 'ඇ': 'a', 'ඈ': 'aa', 'ඉ': 'i', 'ඊ': 'ee', 'උ': 'u', 'ඌ': 'uu','ඍ': 'ru', 'ඎ': 'ruu', 'ඏ': 'lu', 'ඐ': 'luu', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o','ඕ': 'oo', 'ඖ': 'au'}

    consonants = {'ක': 'k', 'ඛ': 'kh', 'ග': 'g', 'ඟ': 'ng', 'ඝ': 'gh', 'ඞ': 'ng', 'ච': 'ch', 'ඡ': 'ch', 'ජ': 'j', 'ඣ': 'jh', 'ඤ': 'ny', 'ට': 't', 'ඨ': 't', 'ඩ': 'd', 'ඪ': 'd', 'ණ': 'n', 'ත': 'th', 'ථ': 'th', 'ද': 'd', 'ඳ': 'nd', 'ධ': 'dh', 'න': 'n', 'ප': 'p', 'ඵ': 'p', 'බ': 'b', 'භ': 'bh', 'ඹ': 'mba', 'ම': 'm', 'ය': 'y', 'ර': 'r', 'ල': 'l', 'ව': 'v', 'ශ': 'sh', 'ෂ': 'sh', 'ස': 's','හ': 'h', 'ළ': 'l', 'ෆ': 'f'}

    vowel_modifiers = {'්': '', 'ා': 'a', 'ැ': 'a', 'ෑ': 'a', 'ි': 'i', 'ී': 'i', 'ු': 'u', 'ූ': 'u','ෙ': 'e', 'ේ': 'e', 'ෛ': 'ai', 'ො': 'o', 'ෝ': 'o', 'ෞ': 'au','ෟ': 'ru', 'ෳ': 'ruu', '්‍ය': 'ya', 'ං': 'n', 'ඃ': 'h', 'ෘ': 'ra'}

    singlish_text = ""
    i = 0
    length = len(sinhala_text)

    while i < length:
        char = sinhala_text[i]

        if char in vowels and i < len(sinhala_text):
            singlish_char = vowels.get(char, vowels.get(char, char))
            singlish_text += singlish_char
            i += 1
            continue

        if char in consonants and i + 1 < len(sinhala_text):
            next_char = sinhala_text[i + 1]

            if next_char in vowel_modifiers:
                combined_char = char + next_char
                singlish_char = consonants.get(combined_char, consonants.get(char, char) + vowel_modifiers.get(next_char, next_char))
                singlish_text += singlish_char
                i += 2
                continue
            else:
                singlish_char = consonants.get(char, consonants.get(char, char))
                singlish_char += 'a'
                singlish_text += singlish_char
                i += 1
                continue

        singlish_text += sinhala_text[i]
        singlish_text = singlish_text.replace(u'\u200D', '')
        i += 1

    return singlish_text

def transliterate_to_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            try:
                data = json.loads(line)
                # Transliterate all values in the dictionary
                for key, value in data.items():
                    if isinstance(value, str):
                        data[key] = sinhala_to_singlish(value)
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

input_file = input("Enter the path to your Sinhala input JSONL file: ")
output_file = input("Enter the desired path for the Singlish output JSONL file: ")

transliterate_to_jsonl(input_file, output_file)