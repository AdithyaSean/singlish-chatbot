from google.cloud import translate_v2 as translate
import json

# Initialize the Google Cloud Translate client
translate_client = translate.Client()

def translate_content_to_sinhala(input_file, output_file):
	with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
		for line in infile:
			# Parse the JSON line
			data = json.loads(line)
			
			# Iterate through each message and translate the 'content'
			for message in data['messages']:
				if 'content' in message:
					# Translate the content to Sinhala
					result = translate_client.translate(message['content'], target_language='si')
					message['content'] = result['translatedText']
			
			# Write the updated JSON line to the output file
			json.dump(data, outfile, ensure_ascii=False)
			outfile.write('\n')

# Specify your input and output file paths
input_file_path = 'datasets/english/english_basic_train_dataset2_part' + input('input file name: ') + '.jsonl'
output_file_path = 'datasets/sinhala/sinhala_basic_train_dataset2_part' + input('output file name: ') + '.jsonl'

# Call the function
translate_content_to_sinhala(input_file_path, output_file_path)