# Day 9: Text Generation with GPT-2
# This script demonstrates generating text using HuggingFace Transformers and GPT-2

from transformers import pipeline

# Create a text generation pipeline with GPT-2
text_generator = pipeline("text-generation", model="gpt2")

# Generate text
prompt = "Artificial Intelligence is"
result = text_generator(prompt, max_length=30)

# Print and save the generated text as an image
generated_text = result[0]['generated_text']
print(generated_text)

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.axis('off')
plt.text(0.01, 0.5, generated_text, fontsize=12, wrap=True)
plt.savefig('Day-9/gpt2_generated_text.png', bbox_inches='tight')
