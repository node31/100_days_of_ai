# Day 10: Model Evaluation Comparison
# This script compares evaluation metrics for two classifiers on the Iris dataset and visualizes confusion matrices

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report

# Load Iris dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Logistic Regression
lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)
acc_lr = accuracy_score(y_test, pred_lr)

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)
acc_rf = accuracy_score(y_test, pred_rf)

# Visualize confusion matrices
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ConfusionMatrixDisplay.from_predictions(y_test, pred_lr, ax=axes[0], cmap='Blues')
axes[0].set_title(f'Logistic Regression\nAccuracy: {acc_lr:.2f}')
ConfusionMatrixDisplay.from_predictions(y_test, pred_rf, ax=axes[1], cmap='Greens')
axes[1].set_title(f'Random Forest\nAccuracy: {acc_rf:.2f}')
plt.tight_layout()
plt.savefig('Day-10/model_evaluation_comparison.png')
plt.show()

print("Logistic Regression Classification Report:\n", classification_report(y_test, pred_lr))
print("Random Forest Classification Report:\n", classification_report(y_test, pred_rf))
