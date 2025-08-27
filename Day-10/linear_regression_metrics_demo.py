# Day 10: Linear Regression Metrics Demo
# This script demonstrates linear regression, calculates MAE and RMSE, and visualizes predictions vs. actual values

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Generate synthetic data (simple regression)
np.random.seed(42)
X = np.linspace(0, 10, 100)
noise = np.random.normal(0, 1, 100)
y = 2 * X + 3 + noise

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

# Train linear regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Visualize predictions vs. actual
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.plot(X_test, y_pred, color='red', alpha=0.5)
plt.title(f'Linear Regression\nMAE: {mae:.2f} | RMSE: {rmse:.2f}')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.tight_layout()
plt.savefig('Day-10/linear_regression_metrics.png')
plt.show()

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
