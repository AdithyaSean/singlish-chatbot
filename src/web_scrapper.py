import requests
from bs4 import BeautifulSoup
import json
from langdetect import detect, LangDetectException

def is_not_english(text):
    try:
        # Detect the language of the text
        return detect(text) != 'en'
    except LangDetectException:
        # If language detection fails, assume it's not English
        return True

def parse_html_to_jsonl(html_content, url):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []
    
    title = soup.title.string if soup.title else ''
    # Filter paragraphs to exclude English content
    paragraphs = [p.get_text() for p in soup.find_all('p') if is_not_english(p.get_text())]
    # Filter links to exclude English content in the link text
    main_link = url
    
    if paragraphs:  # Only add page data if there's non-English content
        page_data = {
            'title': title,
            'paragraphs': paragraphs,
            'links': main_link
        }
        data.append(page_data)
    
    return data

def fetch_website_content(url):
    response = requests.get(url)
    response.raise_for_status()
    # Attempt to get the charset from the content-type header
    content_type = response.headers.get('Content-Type', '')
    if 'charset=' not in content_type:
        # If charset is not specified, assume UTF-8
        response.encoding = 'utf-8'
    return response.text

def save_to_jsonl(data, output_file):
    if data:  # Check if there's any data
        print("Sample data to be saved:", data[0]['paragraphs'][0])  # Print the first paragraph of the first article for verification
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in data:
            json.dump(entry, f, ensure_ascii=False)  # ensure_ascii=False to avoid Unicode escape sequences
            f.write('\n')

def website_to_jsonl(url, output_file):
    html_content = fetch_website_content(url)
    data = parse_html_to_jsonl(html_content, url)
    save_to_jsonl(data, output_file)

url = input('URL of the website that you want to extract: ')
output_file = input('Name the output jsonl file: ')

website_to_jsonl(url, output_file)