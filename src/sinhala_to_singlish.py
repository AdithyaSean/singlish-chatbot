from pandas import read_csv

def sinhala_to_english(sinhala_word):
    """Transliterates a Sinhala word to English letters using a simple mapping."""
    sinhala_mapping = {
    # Vowels
    'අ': 'a', 'ආ': 'aa', 'ඇ': 'ae', 'ඈ': 'aae',
    'ඉ': 'i', 'ඊ': 'ii', 'උ': 'u', 'ඌ': 'uu',
    'ඍ': 'ru', 'ඎ': 'ruu', 'ඏ': 'lu', 'ඐ': 'luu',
    'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o',
    'ඕ': 'oo', 'ඖ': 'au',
    # Consonants
    'ක': 'ka', 'ඛ': 'kha', 'ග': 'ga', 'ඝ': 'gha',
    'ඞ': 'nga', 'ච': 'cha', 'ඡ': 'chha', 'ජ': 'ja',
    'ඣ': 'jha', 'ඤ': 'nya', 'ට': 'ta', 'ඨ': 'ttha',
    'ඩ': 'da', 'ඪ': 'ddha', 'ණ': 'na', 'ත': 'tha',
    'ථ': 'thha', 'ද': 'da', 'ධ': 'ddha', 'න': 'na',
    'ප': 'pa', 'ඵ': 'pha', 'බ': 'ba', 'භ': 'bha',
    'ම': 'ma', 'ය': 'ya', 'ර': 'ra', 'ල': 'la',
    'ව': 'va', 'ශ': 'sha', 'ෂ': 'sha', 'ස': 'sa',
    'හ': 'ha', 'ළ': 'la', 'ෆ': 'fa',
    # Special Characters
    'ං': 'ng', 'ඃ': 'h',
    # Consonant Combinations
    'ක්': 'k',  'ඛ්': 'kh',  'ග්': 'g',  'ඝ්': 'gh',
    'ච්': 'ch', 'ඡ්': 'chh', 'ජ්': 'j',  'ඣ්': 'jh',
    'ට්': 't',  'ඨ්': 'tth', 'ඩ්': 'd',  'ඪ්': 'ddh',
    'ත්': 'th', 'ථ්': 'tth', 'ද්': 'd',  'ධ්': 'dh',
    'ප්': 'p',  'ඵ්': 'ph', 'බ්': 'b',  'භ්': 'bh',
    'ය්': 'y',  'ර්': 'r',  'ල්': 'l',  'ව්': 'v',
    'ශ්': 'sh', 'ෂ්': 'sh', 'ස්': 's',  'ෆ්': 'f',
}
    english_word = ''.join(sinhala_mapping.get(char, char) for char in sinhala_word)
    return english_word

def transliterate_csv(input_file, output_file):
    """Transliterates Sinhala words in a CSV file to English letters."""
    df = read_csv(input_file)

    # Transliterate only the 'text' column
    df['text'] = df['text'].apply(sinhala_to_english)

    df.to_csv(output_file, index=False)

input_file = 'datasets-sinhala/test3.csv'
output_file = 'datasets-singlish/semiSOLD_singlish.csv'

transliterate_csv(input_file, output_file)
