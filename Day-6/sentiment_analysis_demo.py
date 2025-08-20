from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Sample data
texts = [
    "I love this product!",
    "This is the worst experience ever.",
    "Absolutely fantastic service.",
    "I am not happy with the quality.",
    "Terrible service.",
    "Bad experience overall.",
    "Awful, I will not buy again.",
    "Great job, I am very satisfied!",
    "Excellent quality and fast delivery.",
    "Worst purchase I've made.",
    "Not good, very disappointed.",
    "Amazing! Highly recommend.",
    "I hate this.",
    "Best thing ever!",
    "Disappointing and poor quality.",
    "Superb, exceeded my expectations.",
    "Horrible, do not buy.",
    "Very happy with my order.",
    "Unacceptable, very bad.",
    "Loved it!",
    "I enjoyed this!",
    "Enjoyed every moment.",
    "This was a pleasant experience.",
    "I really enjoyed the service.",
    "Enjoyable and satisfying.",
    "Not enjoyable at all.",
    "I did not enjoy this.",
    "Enjoyed the product, will buy again.",
    "I absolutely enjoyed it!",
    "Enjoyed? Not really, it was bad."
]
labels = [
    1, 0, 1, 0, 0, 0, 0, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
    1, 1, 1, 1, 1, 0, 0, 1, 1, 0
]  # 1 = positive, 0 = negative

# Convert text to features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train a model
model = LogisticRegression()
model.fit(X, labels)

# Test the model
test_texts = [
    "I enjoyed this!",
    "Terrible service.",
    "Absolutely loved the experience.",
    "Not what I expected, very bad.",
    "Fantastic and enjoyable!",
    "Awful, will not recommend.",
    "It was okay, nothing special.",
    "I am extremely happy with the results.",
    "Worst ever.",
    "Great job!",
    "I did not enjoy this at all.",
    "Superb service and friendly staff.",
    "Disappointing and frustrating.",
    "Best purchase I've made!",
    "I hate it."
]
X_test = vectorizer.transform(test_texts)
predictions = model.predict(X_test)

for text, pred in zip(test_texts, predictions):
    sentiment = "Positive" if pred == 1 else "Negative"
    print(f"{text} => {sentiment}")
