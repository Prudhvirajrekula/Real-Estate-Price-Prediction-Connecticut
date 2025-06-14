# 🏠 Real Estate Price Prediction App

A full-stack data science project that includes **end-to-end real estate price prediction** using machine learning models and a deployable web app built with Streamlit.

---

## 📘 Project Overview

This project involves:
- Extensive EDA, preprocessing, and feature engineering in a Jupyter Notebook
- Training and evaluation of multiple models: **Random Forest**, **XGBoost**
- Saving trained models using `joblib`
- Deploying a user-facing **Streamlit app** for interactive predictions

---

## 📂 Project Structure

```
📦 RealEstatePriceApp/
├── app.py                              # Streamlit web application
├── requirements.txt                    # Python dependencies
├── README.md                           # Project overview and instructions
├── rf_model.pkl / xgb_model.pkl        # (Optional if hosted on Google Drive)
├── Real_Estate_Sales_2001-2022_GL.csv # Raw dataset used for modeling
└── Real_Estate_Price_Forecasting.ipynb# Full notebook with analysis & modeling
```

---

## 📊 Jupyter Notebook Highlights (`Real_Estate_Price_Forecasting.ipynb`)

This notebook includes the full ML pipeline:

- ✅ Data loading & cleaning
- ✅ Data quality checks & missing value imputation
- ✅ Feature engineering (20+ features including time-based, location-based)
- ✅ Exploratory Data Analysis (EDA)
- ✅ Model training: Random Forest, XGBoost, Linear Regression
- ✅ Cross-validation & hyperparameter tuning
- ✅ Evaluation metrics (RMSE, MAE, R²)
- ✅ Feature importance insights
- ✅ Model saving using `joblib`

---

## 🖥️ Streamlit App Overview (`app.py`)

The Streamlit app allows users to:

- Select a model: **Random Forest** or **XGBoost**
- Enter property details like:
  - 📍 Town and property type
  - 💰 Assessed property value
  - 📅 Planned sale date
- Click a button to **predict the estimated sale price**
- Learn through built-in tooltips and expandable help sections for non-technical users

Models are automatically downloaded from **Google Drive** using `gdown`.

---

## 📦 Setup Instructions

### 🔹 Clone the Repository

```bash
git clone https://github.com/Prudhvirajrekula/Real-Estate-Price-Forecasting-Connecticut.git
cd RealEstatePriceApp
```

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🚀 Example Use Case

> Curious how much your property in Stamford, CT might sell for?  
Just plug in the **assessed value**, **property type**, and **expected sale date**, and let the ML models do the math!

---