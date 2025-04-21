# 🏠 Rent Prediction in Bengaluru, India

This project implements a complete **machine learning pipeline** for predicting house rent prices in Bengaluru, India. It was developed as part of a task for **Nyumabi GmbH**, a company interested in investing in rental properties in India.

---

## 📌 Problem Statement

Nyumabi GmbH wants to estimate property costs in Bengaluru to make informed investment decisions. Using a dataset sourced from Kaggle, this project builds a regression model to predict rental prices based on property features like location, size, total square footage, and number of bathrooms.

---

## 📊 Dataset

- **Source:** [Kaggle - Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data/data)
- The dataset includes attributes such as:
  - Location
  - Size (e.g., 2 BHK, 4 Bedroom)
  - Total square footage
  - Number of bathrooms
  - Price

---

## 🔧 Pipeline Steps

1. **Data Loading & Exploration**
   - Handled missing values and dropped irrelevant features (`area_type`, `availability`, `society`, `balcony`).
   - Explored data distribution, outliers, and relationships between features.

2. **Feature Engineering**
   - Extracted number of BHKs from `size`.
   - Converted `total_sqft` to numerical values, handling inconsistencies.
   - Created new features like `price_per_sqft`.

3. **Outlier Removal**
   - Applied logical rules to remove extreme price-per-square-foot outliers.
   - Removed inconsistent BHK entries using statistical filtering.

4. **Encoding & Preprocessing**
   - Applied one-hot encoding to categorical variables like `location`.
   - Normalized numerical features.

5. **Model Building**
   - Trained and compared several regression models:
     - Linear Regression
     - Lasso Regression
     - Ridge Regression
     - ElasticNet
     - Random Forest Regressor

6. **Model Evaluation**
   - Evaluated using metrics like R² and cross-validation scores.
   - Used GridSearchCV for hyperparameter tuning (where applicable).

---

## 🧪 Results

- The final model offers reasonable predictive performance.
- Random Forest showed the best results in capturing non-linear relationships in the data.

---
