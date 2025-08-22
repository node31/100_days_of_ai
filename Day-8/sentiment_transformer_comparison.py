# Day 8: Sentiment Classification - Traditional vs Transformer
# This script compares a traditional Bag-of-Words model with a Transformer (DistilBERT) for sentiment analysis

import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from transformers import pipeline
import numpy as np

texts = [
    # Training set (0-11)
    "I loved this movie! It was fantastic.",
    "Terrible film. I will not recommend it.",
    "Not good, very disappointing.",
    "Absolutely amazing experience.",
    "I did not enjoy this movie.",
    "Great acting and story.",
    "Awful, waste of time.",
    "Best movie ever!",
    "I enjoy this movie.",
    "I do not enjoy this movie.",
    "The plot was boring and predictable.",
    "Wonderful visuals and soundtrack.",
    # Test set (12-19)
    "I can't say I liked this movie.",
    "I can't say I didn't like this movie.",
    "I really enjoyed the acting, but the story was bad.",
    "Not only was it boring, it was also too long.",
    "I absolutely did not enjoy this film.",
    "I absolutely enjoyed this film.",
    "The movie was not bad at all.",
    "The movie was not good at all."
]
labels = [
    1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1,  # Training
    0, 1, 0, 0, 0, 1, 1, 0               # Test
]  # 1 = positive, 0 = negative

# Split into train and test
train_idx = np.arange(0, 12)
test_idx = np.arange(12, 20)
X_train = [texts[i] for i in train_idx]
y_train = [labels[i] for i in train_idx]
X_test = [texts[i] for i in test_idx]
y_test = [labels[i] for i in test_idx]

# --- Traditional Model (Bag-of-Words) ---
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

clf = LogisticRegression()
clf.fit(X_train_vec, y_train)
preds_bow = clf.predict(X_test_vec)
acc_bow = accuracy_score(y_test, preds_bow)

# --- Transformer Model (DistilBERT) ---
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
preds_transformer = [1 if classifier(text)[0]['label'] == 'POSITIVE' else 0 for text in X_test]
acc_transformer = accuracy_score(y_test, preds_transformer)

# --- Visualization ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ConfusionMatrixDisplay.from_predictions(y_test, preds_bow, ax=axes[0], cmap='Blues')
axes[0].set_title(f'Traditional Model\nAccuracy: {acc_bow:.2f}')
ConfusionMatrixDisplay.from_predictions(y_test, preds_transformer, ax=axes[1], cmap='Greens')
axes[1].set_title(f'Transformer Model\nAccuracy: {acc_transformer:.2f}')
plt.tight_layout()
plt.savefig('Day-8/sentiment_comparison.png')
plt.show()

print("Test Sentences:")
for i, text in enumerate(X_test):
    print(f"{text}\n  True: {'Positive' if y_test[i] else 'Negative'} | Bag-of-Words: {'Positive' if preds_bow[i] else 'Negative'} | Transformer: {'Positive' if preds_transformer[i] else 'Negative'}\n")
