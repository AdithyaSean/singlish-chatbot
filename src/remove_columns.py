import json

input_file_path = 'datasets/singlish/' + input('enter the file name: ') + '.jsonl'
output_file_path = 'datasets/singlish/' + input('enter the output file name: ') + '.jsonl'
column_name = input('enter the column to remove: ')

def remove_columns(input_file_path, output_file_path, column_name):
    with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            json_obj = json.loads(line)
            json_obj.pop(column_name, None)
            output_file.write(json.dumps(json_obj, ensure_ascii=False) + '\n')

remove_columns(input_file_path, output_file_path, column_name)