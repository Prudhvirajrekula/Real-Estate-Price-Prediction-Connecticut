# 🏠 Real Estate Price Prediction App

A full-stack data science project that includes **end-to-end real estate price prediction** using machine learning models and a deployable web app built with Streamlit.

---

## 📘 Project Overview

This project involves:
- Extensive EDA, preprocessing, and feature engineering in a Jupyter Notebook
- Training and evaluation of multiple models: **Random Forest**, **XGBoost**
- Saving trained models using `joblib` (models hosted externally)
- Deploying a user-facing **Streamlit app** for interactive predictions

---

## 🌐 Live Demo

🔗 [Open the Streamlit Web App](https://real-estate-price-forecasting-connecticut-prudhviraj.streamlit.app/)

---

## 📂 Project Structure

```
📦 RealEstatePriceApp/
├── app.py                              # Streamlit web application
├── requirements.txt                    # Python dependencies
├── README.md                           # Project overview and instructions
└── Real_Estate_Price_Forecasting.ipynb # Full notebook with analysis & modeling
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

Models are downloaded from Google Drive using `gdown`.

---

## 📦 Setup Instructions

### 🔹 Clone the Repository

```bash
git clone https://github.com/Prudhvirajrekula/Real-Estate-Price-Prediction-Connecticut.git
cd Real-Estate-Price-Prediction-Connecticut
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

## 📂 Dataset Source

The dataset used for this project is publicly available at:

🔗 [Real Estate Sales 2001–2018 – Data.gov](https://catalog.data.gov/dataset/real-estate-sales-2001-2018)

---
## Screenshots
<img width="1912" height="1082" alt="Realestate" src="https://github.com/user-attachments/assets/f6bd7253-1045-49da-ba9e-56d4c6a308ee" />
<img width="1916" height="1038" alt="Realestate1" src="https://github.com/user-attachments/assets/0e4b4486-8cf3-4676-a1a1-118f7094731e" />

## 🤝 Credits

Built by [Prudhvi Raj Rekula](https://github.com/Prudhvirajrekula)  
Powered by Python, Streamlit, scikit-learn, and XGBoost.
