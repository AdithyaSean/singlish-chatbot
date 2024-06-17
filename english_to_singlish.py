import pandas as pd
import concurrent.futures
from googletrans import Translator
from tqdm import tqdm

def translate_line(line, translator, src='en', dest='si'):
    """Translates a single line using Googletrans."""
    translation = translator.translate(line, src='en', dest='si')
    return translation.pronunciation


def singlishify(input_file, output_file, max_workers=4):
    """Translates an entire CSV dataset using multiprocessing."""

    df = pd.read_csv(input_file)
    total_lines = len(df)
    df['id'] = range(1, total_lines + 1)  # Directly assign range to 'id'
    df = df[['id', 'title', 'text']]

    # Use multiprocessing to parallelize translation
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        translator = Translator()  # Create a Translator instance outside the loop

        with tqdm(total=total_lines, desc="Translating") as pbar:
            singlish_titles = list(executor.map(lambda line: translate_line(line, translator, src='en', dest='si'), df['title']))
            singlish_texts = list(executor.map(lambda line: translate_line(line, translator, src='en', dest='si'), df['text']))
            pbar.update(total_lines)  # Update the progress bar to 100%

    # Update the 'title' and 'text' columns with translated values
    df['title'] = singlish_titles
    df['text'] = singlish_texts

    df.to_csv(output_file, index=False, encoding='utf-8')

input_file = 'datasets-english/train-00000-of-00041.csv'
output_file = 'datasets-singlish/train-00000-of-00041.csv'

singlishify(input_file, output_file)
