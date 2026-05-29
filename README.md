# 🛒 BigMart Sales Prediction using Machine Learning

A Machine Learning project that predicts product sales for BigMart stores using historical sales data and the XGBoost Regression algorithm.

## 📌 Project Overview

The goal of this project is to build a predictive model that estimates the sales of products across different BigMart outlets.

Accurate sales prediction helps businesses:

- Improve inventory management
- Optimize supply chain operations
- Increase profitability
- Make data-driven business decisions

---

## 📂 Dataset

The project uses:

- Train.csv
- Test.csv

### Features Included

- Item Weight
- Item Fat Content
- Item Visibility
- Item Type
- Item MRP
- Outlet Establishment Year
- Outlet Size
- Outlet Location Type
- Outlet Type

### Target Variable

```text
Item_Outlet_Sales
```

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost

---

## 📦 Required Libraries

Install dependencies using:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost
```

---

## 🚀 Project Workflow

### 1. Import Libraries

Load all required Python libraries for data analysis, visualization, and machine learning.

### 2. Load Dataset

Read the training dataset using Pandas.

### 3. Data Cleaning

Handle missing values:

- Item_Weight → Mean Imputation
- Outlet_Size → Mode Imputation

### 4. Feature Engineering

Remove unnecessary columns:

- Item_Identifier
- Outlet_Identifier

Convert categorical variables into numerical format using One-Hot Encoding.

### 5. Train-Test Split

Split dataset into:

- 80% Training Data
- 20% Testing Data

### 6. Model Training

Train an XGBoost Regressor model on the processed dataset.

### 7. Prediction

Generate sales predictions on test data.

### 8. Evaluation

Evaluate model performance using:

```text
R² Score
```

### 9. Visualization

Plot Actual Sales vs Predicted Sales.

---

## 📈 Machine Learning Model

### XGBoost Regressor

XGBoost is an advanced gradient boosting algorithm known for:

- High accuracy
- Fast training
- Excellent performance on tabular datasets
- Handling complex relationships between features

---

## 📊 Evaluation Metric

### R² Score

Measures how well predicted values match actual sales values.

Formula:

```text
R² = 1 - (Residual Sum of Squares / Total Sum of Squares)
```

Higher R² Score indicates better model performance.

---

## 📁 Project Structure

```text
BigMart-Sales-Prediction/
│
├── Train.csv
├── Test.csv
├── bigmart.py
├── README.md
│
└── requirements.txt
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/BigMart-Sales-Prediction.git
```

Move into the project directory:

```bash
cd BigMart-Sales-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python bigmart.py
```

---

## 📷 Output

The model provides:

- Predicted Sales Values
- R² Performance Score
- Actual vs Predicted Scatter Plot

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Feature Scaling
- Cross Validation
- Model Comparison
- Streamlit Web App Deployment
- Real-time Prediction System

---

## 👨‍💻 Author

Developed as a Machine Learning project for sales forecasting and predictive analytics.

---

## ⭐ If you found this project useful

Give this repository a star ⭐ and share it with others.
