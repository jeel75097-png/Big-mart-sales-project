# ================================
# 📦 Import Libraries
# ================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn import metrics
from xgboost import XGBRegressor

# ================================
# 📂 Load Dataset
# ================================
# 👉 Make sure Train.csv is in same folder
data = pd.read_csv('Train.csv')

# ================================
# 🔍 Basic Info
# ================================
print(data.head())
print(data.info())

# ================================
# 🧹 Handle Missing Values
# ================================
# Numerical
data['Item_Weight'].fillna(data['Item_Weight'].mean(), inplace=True)

# Categorical
data['Outlet_Size'].fillna(data['Outlet_Size'].mode()[0], inplace=True)

# ================================
# ❌ Drop useless ID columns
# ================================
data = data.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1)

# ================================
# 🔄 Convert Categorical → Numeric
# ================================
data = pd.get_dummies(data, drop_first=True)

# ================================
# 🎯 Split Features & Target
# ================================
X = data.drop('Item_Outlet_Sales', axis=1)
y = data['Item_Outlet_Sales']

# ================================
# 🔀 Train Test Split
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2
)

# ================================
# 🤖 Model Training (XGBoost)
# ================================
model = XGBRegressor()

model.fit(X_train, y_train)

# ================================
# 📊 Prediction
# ================================
y_pred = model.predict(X_test)

# ================================
# 📈 Evaluation
# ================================
r2 = metrics.r2_score(y_test, y_pred)
print("R2 Score:", r2)

# ================================
# 📉 Plot Actual vs Predicted
# ================================
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted")
plt.show()