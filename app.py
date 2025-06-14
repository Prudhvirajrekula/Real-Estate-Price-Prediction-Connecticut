import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tempfile
import gdown
from datetime import datetime

# ----------------------- Helper Functions ----------------------------

@st.cache_data
def download_model_from_drive(file_id):
    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".joblib").name
    try:
        gdown.download(id=file_id, output=output_path, quiet=True)
        return output_path
    except Exception as e:
        st.error(f"❌ Model download failed: {str(e)}")
        return None

def create_features(sale_date, assessed_value, property_type, town):
    date_obj = pd.to_datetime(sale_date)
    return pd.DataFrame({
        "Assessed Value": [assessed_value],
        "Year": [date_obj.year],
        "Month": [date_obj.month],
        "Quarter": [date_obj.quarter],
        "DayOfWeek": [date_obj.weekday()],
        "Latitude": [0.0],  # placeholder
        "Longitude": [0.0],  # placeholder
        "Town_" + town: [1],
        "PropType_" + property_type: [1],
    })

# ----------------------- UI ----------------------------

st.title("🏠 Connecticut Real Estate Price Prediction")
st.markdown("""
This app predicts **real estate sale prices** using trained ML models (Random Forest & XGBoost).
""")

# ----------------------- INFO BOX ----------------------------

with st.expander("ℹ️ What does this app do?"):
    st.markdown("""
    This application allows you to estimate the **future sale price** of a property in Connecticut.
    
    You'll input basic details like:
    - Assessed property value
    - Sale date
    - Property type
    - Town location
    
    Then the app uses a trained Machine Learning model to give you a predicted price.
    """)

# ----------------------- Input Fields with Help ----------------------------

assessed_value = st.number_input(
    "💰 Assessed Property Value ($)",
    min_value=1000,
    step=1000,
    help="This is the value assigned by tax assessors. It’s not the market price but used for tax purposes."
)

sale_date = st.date_input(
    "📅 Sale Date",
    value=datetime(2022, 1, 1),
    help="The date you plan to sell or evaluate the property."
)

property_type = st.selectbox(
    "🏗️ Property Type",
    [
        "Commercial", "Condo", "Four Family", "Industrial", "Public Utility",
        "Residential", "Single Family", "Three Family", "Two Family", "Vacant Land"
    ],
    help="Choose the category that best describes the property."
)

town = st.selectbox(
    "🏙️ Select Town",
    [
        "Andover", "Ansonia", "Avon", "Bridgeport", "Bristol", "Danbury", "East Hartford",
        "Fairfield", "Greenwich", "Hartford", "Manchester", "Meriden", "Middletown",
        "Milford", "New Britain", "New Haven", "Norwalk", "Stamford", "Stratford", "Waterbury"
    ],
    help="Select the town where the property is located."
)

model_choice = st.selectbox(
    "🤖 Choose a Model",
    ["Random Forest", "XGBoost"],
    help="Random Forest is simple and interpretable. XGBoost is more advanced and often more accurate."
)

# ----------------------- Model File IDs ----------------------------

model_file_ids = {
    "Random Forest": "1rCjOLocgwSYJDyuNAxwo6Y8QF4UIdtEe",
    "XGBoost": "1DD3nCrJ5CTfQlgeGvDrAFb_1r90UWJmx"
}

# ----------------------- Prediction ----------------------------

if st.button("💡 Predict Sale Price"):
    with st.spinner("🔄 Downloading model and making prediction..."):
        model_path = download_model_from_drive(model_file_ids[model_choice])
        if model_path:
            try:
                model = joblib.load(model_path)
                input_df = create_features(sale_date, assessed_value, property_type, town)
                all_features = model.feature_names_in_
                input_df = input_df.reindex(columns=all_features, fill_value=0)

                prediction = model.predict(input_df)[0]
                st.success(f"🏷️ **Predicted Sale Price** ({model_choice}): ${prediction:,.2f}")
            except Exception as e:
                st.error(f"❌ Prediction failed: {str(e)}")

# ----------------------- Footer ----------------------------

st.markdown("---")
st.caption("📊 Powered by Machine Learning | Created by Prudhvi Raj Rekula")