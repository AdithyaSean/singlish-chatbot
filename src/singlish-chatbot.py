import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="211555470797", location="us-central1")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.9,
    "top_p": 1
}
model = TextGenerationModel.from_pretrained("text-bison@002")
model = model.get_tuned_model("projects/211555470797/locations/us-central1/models/6051651526139576320")
response = model.predict(
    """oyata kohomada?""",
    **parameters
)
print(f"Response from Model: {response.text}")