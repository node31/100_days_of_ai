# Day 13: Azure OpenAI API Demo
# This script sends a prompt to Azure OpenAI GPT-4.1 and visualizes the response

import requests
import json
import matplotlib.pyplot as plt

endpoint = ""
api_key = ""
headers = {
	"Content-Type": "application/json",
	"api-key": api_key
}
payload = {
	"messages": [
		{"role": "user", "content": "Tell me about the future of AI."}
	],
	"max_tokens": 100
}
response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
result = response.json()

# Extract the model's reply
reply = result.get('choices', [{}])[0].get('message', {}).get('content', 'No response')

# Visualize the response as an image
plt.figure(figsize=(8, 6))
plt.axis('off')
plt.text(0.01, 0.5, reply, fontsize=12, wrap=True)
plt.savefig('Day-13/azure_openai_response.png', bbox_inches='tight')
# Day 13: Experimenting with Azure OpenAI API – Demo
