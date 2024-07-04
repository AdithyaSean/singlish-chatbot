import json
import re

def sinhala_to_singlish(sinhala_text):
    vowels = {'අ': 'a', 'ආ': 'aa', 'ඇ': 'a', 'ඈ': 'aa', 'ඉ': 'i', 'ඊ': 'ee', 'උ': 'u', 'ඌ': 'uu','ඍ': 'ru', 'ඎ': 'ruu', 'ඏ': 'lu', 'ඐ': 'luu', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o','ඕ': 'oo', 'ඖ': 'au', 'ං': 'an', 'ඃ': 'h',}
    consonants = {'ක': 'k', 'ඛ': 'kh', 'ග': 'g', 'ඟ': 'ng', 'ඝ': 'gh', 'ඞ': 'ng', 'ච': 'ch', 'ඡ': 'ch', 'ජ': 'j', 'ඣ': 'jh', 'ඤ': 'ny', 'ඥ': 'gny', 'ට': 't', 'ඨ': 't', 'ඩ': 'd', 'ඬ': 'nd', 'ඪ': 'd', 'ණ': 'n', 'ත': 'th', 'ථ': 'th', 'ද': 'd', 'ඳ': 'nd', 'ධ': 'dh', 'න': 'n', 'ප': 'p', 'ඵ': 'p', 'බ': 'b', 'භ': 'bh', 'ඹ': 'mba', 'ම': 'm', 'ය': 'y', 'ර': 'r', 'ල': 'l', 'ව': 'v', 'ශ': 'sh', 'ෂ': 'sh', 'ස': 's','හ': 'h', 'ළ': 'l', 'ෆ': 'f'}
    vowel_modifiers = {'්': '', 'ා': 'a', 'ැ': 'a', 'ෑ': 'a', 'ි': 'i', 'ී': 'i', 'ු': 'u', 'ූ': 'u','ෙ': 'e', 'ේ': 'e', 'ෛ': 'ai', 'ො': 'o', 'ෝ': 'o', 'ෞ': 'au','ෟ': 'ru', 'ෳ': 'ruu', '්‍ය': 'ya', 'ෘ': 'ru'}
    characters_to_remove = r'[\u200B\u200C\u200D\u2060\u2061\u2062\u2063\u2064\uFEFF\u00AD\u180E\u200E\u200F\u202A\u202B\u202C\u202D\u202E\u2018\u2019\u201a\u201b\u201c\u201d\u201e\u201f\u2020\u2021\u2022\u2023\u2024\u2025\u2026\u2027\u2028\u2029\u202A\u202B\u202C\u202D\u202E\u202F\u2030\u2031\u2032\u2033\u2034\u2035\u2036\u2037\u2038\u2039\u203A\u203B\u203C\u203D\u203E\u203F\u2040\u2041\u2042\u2043\u2044\u2045\u2046\u2047\u2048\u2049\u204A\u204B\u204C\u204D\u204E\u204F\u2050\u2051\u2052\u2053\u2054\u2055\u2056\u2057\u2058\u2059\u205A\u205B\u205C\u205D\u205E\u205F\u2060\u2061\u2062\u2063\u2064\u2065\u2066\u2067\u2068\u2069\u206A\u206B\u206C\u206D\u206E\u206F\uFEFF\uFFF9\uFFFA\uFFFB\uFFFC\uFFFD\uFFFE\uFFFF\u200B\u200C\u200D\u200E\u200F\u202A\u202B\u202C\u202D\u202E\u202F\u2060\u2061\u2062\u2063\u2064\u2065\u2066\u2067\u2068\u2069\u206A\u206B\u206C\u206D\u206E\u206F\uFEFF\uFFF9\uFFFA\uFFFB\uFFFC\uFFFD\uFFFE\uFFFF\u200B\u200C\u200D\u200E\u200F\u202A\u202B\u202C\u202D\u202E\u202F\u2060\u2061\u2062\u2063\u2064\u2065\u2066\u2067\u2068\u2069\u206A\u206B\u206C\u206D\u206E\u206F\uFEFF\uFFF9\uFFFA\uFFFB\uFFFC\uFFFD\uFFFE\uFFFF\u200B\u1308B\u1309D\u131F3\u13216\u132AA\u132B5\u133CF\u133E0\u1F1CB\u1F615\u00A2\u00A3\u00A7\u00AB\u00AE\u00AF\u00B0\u00B5\u00B7\u00BA\u00BB\u00BD\u00C1\u00C2\u00C6\u00C7\u00C9\u00CD\u00D3\u00D6\u00D7\u00DA\u00DC\u00DE\u00DF\u00E0\u00E1\u00E2\u00E4\u00E5\u00E6\u00E7\u00E8\u00E9\u00EA\u00EB\u00ED\u00EE\u00EF\u00F0\u00F1\u00F2\u00F3\u00F4\u00F6\u00F8\u00F9\u00FA\u00FC\u00FD\u00FE\u0101\u0107\u010D\u0113\u011B\u011F\u012A\u012B\u0131\u014D\u0153\u0159\u015A\u015B\u015F\u0160\u0161\u016B\u01CE\u01D0\u0245\u025B\u027E\u0295\u02BB\u02D0\u0301\u0303\u0304\u0392\u0394\u039B\u039E\u03A7\u03A8\u03AC\u03AD\u03AE\u03AF\u03B1\u03B2\u03B3\u03B4\u03B5\u03B7\u03B8\u03B9\u03BA\u03BB\u03BC\u03BD\u03BE\u03BF\u03C0\u03C1\u03C2\u03C3\u03C4\u03C5\u03C6\u03C7\u03C9\u03CC\u03CD\u03DA\u03E8\u0411\u0412\u0413\u0414\u0415\u0418\u0419\u041A\u041B\u041C\u041D\u041E\u0420\u0421\u0422\u0423\u0424\u0425\u0430\u0431\u0432\u0433\u0434\u0435\u0437\u0438\u0439\u043A\u043B\u043C\u043D\u043E\u0440\u0441\u0442\u0443\u0445\u0446\u0447\u0448\u044B\u044C\u044E\u044F\u0456\u05D0\u05D3\u05D4\u05D6\u05DA\u05DC\u05E8\u0623\u0627\u0629\u062A\u062E\u062F\u0631\u0633\u0641\u0643\u0644\u0645\u0647\u064A\u0DCA\u0DCF\u0DD9\u0DF2\u1E25\u1E35\u1E6D\u1F00\u1F04\u1F10\u1F11\u1F15\u1F21\u1F26\u1F30\u1F36\u1F37\u1F41\u1F44\u1F50\u1F70\u1F72\u1F74\u1F78\u1FC7\u1FE6\u2013\u2014\u2082\u2083\u2084\u2122\u2153\u2154\u2191\u2192\u2202\u2212\u221A\u221D\u221E\u2225\u222B\u2260\u2C81\u2C8F\u2C99\u2C9B\u2C9F\u2CA1\u2CA3\u2CA7\u2CA9\u2CB1\u3046\u304E\u3057\u305A\u3063\u306B\u306F\u307F\u3083\u3087\u3089\u3093\u30A6\u30C4\u30CB\u30CF\u30E7\u4E0A\u4E50\u4E66\u4EE4\u4F2F\u4FDD\u502D\u5143\u5149\u514B\u5175\u5200\u5208\u52D9\u52FE\u5305\u5370\u53F2\u53F7\u53F8\u5434\u5546\u56DB\u56FD\u591A\u5937\u593E\u5B50\u5B8B\u5BF6\u5C71\u5E1D\u5E74\u5EC3\u5FC3\u64B0\u6689\u66F8\u6708\u675C\u6771\u695A\u6B4C\u6C49\u6CBB\u6CD5\u6CE2\u6CF0\u6E05\u6FC2\u7063\u738B\u767E\u7687\u7995\u7B19\u7B49\u7C73\u7CE7\u7D4C\u7F57\u7F85\u803B\u8089\u81FA\u821E\u822C\u82E5\u871C\u8861\u8A18\u8BA4\u8BBA\u8D8A\u8DF5\u901A\u9053\u9077\u9326\u961F\u96DC\u9762\u9806\u982D\u98CE\u9905\u9928\u9943\u9945\u99AC\u9A6C\u9ECE\uA725\ud80c\udc8b\ud80c\udc9d\ud80c\uddf3\u305f\ud83d\ude15\ud83c\uddcb\ud80c\udfe0\ud80c\ude16\ud80c\udeb5\ud80c\udfcf\ud80c\udeaa]'
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