import json
import re



def sinhala_to_singlish(sinhala_text):
    vowels = {'අ': 'a', 'ආ': 'aa', 'ඇ': 'a', 'ඈ': 'aa', 'ඉ': 'i', 'ඊ': 'ee', 'උ': 'u', 'ඌ': 'uu','ඍ': 'ru', 'ඎ': 'ruu', 'ඏ': 'lu', 'ඐ': 'luu', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o','ඕ': 'oo', 'ඖ': 'au'}
    consonants = {'ක': 'k', 'ඛ': 'kh', 'ග': 'g', 'ඟ': 'ng', 'ඝ': 'gh', 'ඞ': 'ng', 'ච': 'ch', 'ඡ': 'ch', 'ජ': 'j', 'ඣ': 'jh', 'ඤ': 'ny', 'ට': 't', 'ඨ': 't', 'ඩ': 'd', 'ඬ': 'nd', 'ඪ': 'd', 'ණ': 'n', 'ත': 'th', 'ථ': 'th', 'ද': 'd', 'ඳ': 'nd', 'ධ': 'dh', 'න': 'n', 'ප': 'p', 'ඵ': 'p', 'බ': 'b', 'භ': 'bh', 'ඹ': 'mba', 'ම': 'm', 'ය': 'y', 'ර': 'r', 'ල': 'l', 'ව': 'v', 'ශ': 'sh', 'ෂ': 'sh', 'ස': 's','හ': 'h', 'ළ': 'l', 'ෆ': 'f'}
    vowel_modifiers = {'්': '', 'ා': 'a', 'ැ': 'a', 'ෑ': 'a', 'ි': 'i', 'ී': 'i', 'ු': 'u', 'ූ': 'u','ෙ': 'e', 'ේ': 'e', 'ෛ': 'ai', 'ො': 'o', 'ෝ': 'o', 'ෞ': 'au','ෟ': 'ru', 'ෳ': 'ruu', '්‍ය': 'ya', 'ං': 'an', 'ඃ': 'h', 'ෘ': 'ru'}

    invisible_characters = r'[\u200D\u200C\u2063]'


    singlish_text = ""
    i = 0

    while i < len(sinhala_text):
        singlish_text.replace(u'\u200D\u200C\u2063', '')
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
            
    singlish_text = re.sub(invisible_characters, '', singlish_text)
    return singlish_text

def transliterate_to_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            try:
                data = json.loads(line)
                for key, value in data.items():
                    if isinstance(value, str):
                        data[key] = sinhala_to_singlish(value)
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

input_file = input("Enter the path to your Sinhala input JSONL file: ")
output_file = input("Enter the desired path for the Singlish output JSONL file: ")

transliterate_to_jsonl(input_file, output_file)