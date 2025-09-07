# Day 14: HuggingFace Transformers Demo
# This script loads a pre-trained transformer model and performs text classification

from transformers import pipeline
import matplotlib.pyplot as plt

# Create a text classification pipeline using a pre-trained model
classifier = pipeline('sentiment-analysis')

# Sample texts to classify
texts = [
    "I love using HuggingFace Transformers!",
    "This is a terrible experience.",
    "The model works well for NLP tasks.",
    "I'm not sure about the results."
]

# Get predictions
results = classifier(texts)
labels = [result['label'] for result in results]
scores = [result['score'] for result in results]

# Visualize the results
plt.figure(figsize=(8, 5))
plt.barh(texts, scores, color=['green' if label == 'POSITIVE' else 'red' for label in labels])
plt.xlabel('Confidence Score')
plt.title('Sentiment Classification with HuggingFace Transformers')
plt.tight_layout()
plt.savefig('Day-14/huggingface_transformers_results.png')
