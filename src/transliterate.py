import json
import re

def sinhala_to_singlish(sinhala_text):
    vowels = {'අ': 'a', 'ආ': 'aa', 'ඇ': 'a', 'ඈ': 'aa', 'ඉ': 'i', 'ඊ': 'ee', 'උ': 'u', 'ඌ': 'uu','ඍ': 'ru', 'ඎ': 'ruu', 'ඏ': 'lu', 'ඐ': 'luu', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o','ඕ': 'oo', 'ඖ': 'au', 'ං': 'n', 'ඃ': 'h'}
    consonants = {'ක': 'k', 'ඛ': 'kh', 'ග': 'g', 'ඟ': 'ng', 'ඝ': 'gh', 'ඞ': 'ng', 'ච': 'ch', 'ඡ': 'ch', 'ජ': 'j', 'ඣ': 'jh', 'ඤ': 'ny', 'ඥ': 'gny', 'ට': 't', 'ඨ': 't', 'ඩ': 'd', 'ඬ': 'nd', 'ඪ': 'd', 'ණ': 'n', 'ත': 'th', 'ථ': 'th', 'ද': 'd', 'ඳ': 'nd', 'ධ': 'dh', 'න': 'n', 'ප': 'p', 'ඵ': 'p', 'බ': 'b', 'භ': 'bh', 'ඹ': 'mba', 'ම': 'm', 'ය': 'y', 'ර': 'r', 'ල': 'l', 'ව': 'w', 'ශ': 'sh', 'ෂ': 'sh', 'ස': 's','හ': 'h', 'ළ': 'l', 'ෆ': 'f'}
    vowel_modifiers = {'්': '', 'ා': 'a', 'ැ': 'a', 'ෑ': 'a', 'ි': 'i', 'ී': 'i', 'ු': 'u', 'ූ': 'u','ෙ': 'e', 'ේ': 'e', 'ෛ': 'ai', 'ො': 'o', 'ෝ': 'o', 'ෞ': 'au','ෟ': 'ru', 'ෳ': 'ruu', '්‍ය': 'ya', 'ෘ': 'ru'}
    characters_to_remove = r'[\u200B-\u200F\u202A-\u202E\u2060-\u2064\u2065-\u2069\u206A-\u206F\uFEFF\uFFF9-\uFFFD]'
    singlish_text = ""
    i = 0

    while i < len(sinhala_text):
        if sinhala_text[i] in vowels:
            singlish_text += vowels.get(sinhala_text[i])
            i += 1

        elif sinhala_text[i] in consonants:
            singlish_text += consonants.get(sinhala_text[i])
            i += 1

            if i < len(sinhala_text) and sinhala_text[i] in vowel_modifiers:
                singlish_text += vowel_modifiers.get(sinhala_text[i])
                i += 1

                if i < len(sinhala_text) and sinhala_text[i] in vowel_modifiers:
                    singlish_text += vowel_modifiers.get(sinhala_text[i])
                    i += 1

            else:
                singlish_text += 'a'

        else:
            singlish_text += sinhala_text[i]
            i += 1

    singlish_text = re.sub(characters_to_remove, '', singlish_text)
    return singlish_text

def transliterate_value(value):
    if isinstance(value, str):
        return sinhala_to_singlish(value)
    elif isinstance(value, dict):
        return {k: transliterate_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [transliterate_value(item) for item in value]
    else:
        return value

def transliterate_to_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            try:
                data = json.loads(line)
                transliterated_data = transliterate_value(data)
                outfile.write(json.dumps(transliterated_data, ensure_ascii=False) + '\n')
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                
input_file = 'datasets/sinhala/sinhala_basic_train_dataset2_part' + input("Name of your input file: ") + '.jsonl'
output_file = 'datasets/singlish/singlish_basic_train_dataset2_part' + input("Name of your output file: ") + '.jsonl'

transliterate_to_jsonl(input_file, output_file)