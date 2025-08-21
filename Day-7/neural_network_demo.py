from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Load the digits dataset (handwritten digit images 0-9)
digits = load_digits()
X, y = digits.data, digits.target

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build a simple neural network (MLP)
mlp = MLPClassifier(hidden_layer_sizes=(32, 16), activation='relu', max_iter=1000, random_state=42)
mlp.fit(X_train, y_train)

# Predict on test set
y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Visualize a few test images and predictions
import numpy as np
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.flat):
	idx = np.random.randint(0, X_test.shape[0])
	ax.imshow(X_test[idx].reshape(8, 8), cmap='gray')
	ax.set_title(f"True: {y_test[idx]}\nPred: {y_pred[idx]}")
	ax.axis('off')
plt.tight_layout()
plt.show()
