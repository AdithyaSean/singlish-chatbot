def split_jsonl_file(input_file, lines_per_file):
	# Initialize variables for tracking
	file_count = 1
	current_line_count = 0
	
	# Open the input file
	with open(input_file, 'r', encoding='utf-8') as infile:
		# Prepare the first output file
		outfile_name = f"{input_file.rsplit('.', 1)[0]}_part{file_count}.jsonl"
		outfile = open(outfile_name, 'w', encoding='utf-8')
		
		# Iterate over each line in the input file
		for line in infile:
			# Write the current line to the current output file
			outfile.write(line)
			current_line_count += 1
			
			# Check if the current output file has reached the desired number of lines
			if current_line_count >= lines_per_file:
				# Close the current output file
				outfile.close()
				# Prepare for the next output file
				file_count += 1
				current_line_count = 0
				outfile_name = f"{input_file.rsplit('.', 1)[0]}_part{file_count}.jsonl"
				outfile = open(outfile_name, 'w', encoding='utf-8')
		
		# Close the last output file
		outfile.close()

# Example usage
split_jsonl_file('datasets/singlish/singlish_reddit_train_dataset2.jsonl', 500)