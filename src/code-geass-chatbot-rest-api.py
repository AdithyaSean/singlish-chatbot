from flask import Flask, request, jsonify
import vertexai
from vertexai.language_models import TextGenerationModel

app = Flask(__name__)

vertexai.init(project="211555470797", location="us-central1")
model = TextGenerationModel.from_pretrained("text-bison@002")
model = model.get_tuned_model("projects/211555470797/locations/us-central1/models/6051651526139576320")

@app.route('/predict', methods=['POST'])
def predict():
	data = request.json
	input_text = data.get("text", "")
	parameters = {
		"candidate_count": 1,
		"max_output_tokens": 1024,
		"temperature": 0.9,
		"top_p": 1
	}
	response = model.predict(input_text, **parameters)
	return jsonify({"response": response.text})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)