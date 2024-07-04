import json

# Create an empty list
reddit_data = []

# Open the file
with open('datasets/singlish/reddit_tuning_dataset.jsonl', 'r', encoding='utf-8') as file:
    # Iterate over each line
    for line in file:
        # Parse the line as JSON
        data = json.loads(line)
        # Append the data to the list
        reddit_data.append(data)

# Function to convert the data to the required format
def convert_to_required_format(data):
    formatted_data = []
    for item in data:
        # Splitting the completion to separate the user content and the model response
        user_content, model_response = item["completion"].split(" -> ")
        formatted_item = {
            "messages": [
                {"role": "user", "content": user_content},
                {"role": "model", "content": model_response}
            ]
        }
        formatted_data.append(formatted_item)
    return formatted_data

# Convert the reddit_data to the required format
converted_data = convert_to_required_format(reddit_data)

# Print or save the converted data
print(json.dumps(converted_data, indent=2))