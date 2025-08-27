# Day 10: Ethics & Safety in AI – Bias Detection Demo
# This script demonstrates bias detection in a simple sentiment analysis model and visualizes prediction differences

import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np


# Expanded training data with more variety and some artificial bias
sentences = [
    "He is a great doctor.", "She is a great doctor.",
    "He is a great nurse.", "She is a great nurse.",
    "He is a great engineer.", "She is a great engineer.",
    "He is a great teacher.", "She is a great teacher.",
    "He is a terrible doctor.", "She is a terrible doctor.",
    "He is a terrible nurse.", "She is a terrible nurse.",
    "He is a terrible engineer.", "She is a terrible engineer.",
    "He is a terrible teacher.", "She is a terrible teacher.",
    # Add some biased data (more positive for male doctors, more negative for female engineers)
    "He is an excellent doctor.", "He is a wonderful doctor.",
    "She is a poor engineer.", "She is a bad engineer."
]
labels = [
    1, 1, 1, 1, 1, 1, 1, 1,   # great
    0, 0, 0, 0, 0, 0, 0, 0,   # terrible
    1, 1,                     # excellent/wonderful doctor (male)
    0, 0                      # poor/bad engineer (female)
]

# Train a simple sentiment model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)
model = LogisticRegression()
model.fit(X, labels)


# Predict on more diverse gender/profession pairs
professions = ["doctor", "nurse", "engineer", "teacher"]
genders = ["He", "She"]
test_templates = [
    "{gender} is a great {profession}.",
    "{gender} is a terrible {profession}.",
    "{gender} is an average {profession}.",
    "{gender} is an excellent {profession}.",
    "{gender} is a poor {profession}."
]
pred_matrix = np.zeros((len(genders), len(professions)))
for i, gender in enumerate(genders):
    for j, profession in enumerate(professions):
        # Use a mix of templates for each cell and average the predictions
        preds = []
        for template in test_templates:
            test_sentence = template.format(gender=gender, profession=profession)
            X_test = vectorizer.transform([test_sentence])
            pred = model.predict(X_test)[0]
            preds.append(pred)
        pred_matrix[i, j] = np.mean(preds)

# Visualize bias (heatmap)
plt.figure(figsize=(6, 4))
plt.imshow(pred_matrix, cmap='coolwarm', vmin=0, vmax=1)
plt.xticks(range(len(professions)), professions)
plt.yticks(range(len(genders)), genders)
plt.xlabel('Profession')
plt.ylabel('Gender')
plt.title('Predicted Sentiment by Gender & Profession')
plt.colorbar(label='Predicted Sentiment (1=Positive, 0=Negative)')
plt.tight_layout()
plt.savefig('Day-10/ai_bias_heatmap.png')
plt.show()
