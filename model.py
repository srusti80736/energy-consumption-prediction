import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

# ML models
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Evaluation metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error


# -----------------------------
# 1 Load dataset
# -----------------------------

df = pd.read_csv("dataset/AEP_hourly.csv")

print("Dataset Loaded Successfully")

# Convert datetime column
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Set datetime as index
df = df.set_index("Datetime")

# Rename energy column
df = df.rename(columns={"AEP_MW": "energy"})


# -----------------------------
# 2 Feature Engineering
# -----------------------------

# Time features
df['hour'] = df.index.hour
df['dayofweek'] = df.index.dayofweek
df['month'] = df.index.month

# Lag features
df['lag1'] = df['energy'].shift(1)
df['lag24'] = df['energy'].shift(24)

# Remove NaN rows
df = df.dropna()

print("Feature Engineering Completed")


# -----------------------------
# 3 Train Test Split
# -----------------------------

train = df[df.index < "2017-01-01"]
test = df[df.index >= "2017-01-01"]

features = ['hour', 'dayofweek', 'month', 'lag1', 'lag24']

X_train = train[features]
y_train = train['energy']

X_test = test[features]
y_test = test['energy']

print("Train-Test Split Completed")


# -----------------------------
# 4 Train Models
# -----------------------------

lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100)

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

print("Models Trained Successfully")


# -----------------------------
# 5 Model Evaluation
# -----------------------------

lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)

lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))

print("\nModel Performance")

print("Linear Regression RMSE:", lr_rmse)
print("Random Forest RMSE:", rf_rmse)


# -----------------------------
# 6 Feature Importance
# -----------------------------

importances = rf.feature_importances_

plt.bar(features, importances)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.show()


# -----------------------------
# 7 Energy Consumption Plot
# -----------------------------

df['energy'].plot(figsize=(12,5))

plt.title("Energy Consumption Over Time")
plt.xlabel("Time")
plt.ylabel("Energy (MW)")
plt.show()


# -----------------------------
# 8 Select Best Model
# -----------------------------

if rf_rmse < lr_rmse:
    best_model = rf
    print("Random Forest Selected")
else:
    best_model = lr
    print("Linear Regression Selected")


# -----------------------------
# 9 Save Model
# -----------------------------

pickle.dump(best_model, open("energy_model.pkl", "wb"))

print("Model saved successfully")