import streamlit as st
import pandas as pd
from joblib import load

# Load the pre-trained model and columns
model = load('rent_model.joblib')
model_columns = load('model_columns.joblib')

# Function to predict rent from input
def predict_rent(location, total_sqft, bhk, bath):
    input_data = pd.DataFrame([{
        'location': location,
        'total_sqft': total_sqft,
        'bath': bath,
        'bhk': bhk
    }])

    # One-hot encode the input data
    input_encoded = pd.get_dummies(input_data)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict rent
    predicted_rent = model.predict(input_encoded)[0]
    return predicted_rent

# Streamlit UI
def main():
    st.title("Rent Prediction Tool")
    st.markdown("Enter the details below to predict the rent.")

    # User input fields
    location = st.text_input("Location", "Example Location")
    total_sqft = st.number_input("Total Square Feet", min_value=1, value=1000)
    bhk = st.number_input("BHK (Bedrooms)", min_value=1, value=2)
    bath = st.number_input("Number of Bathrooms", min_value=1, value=1)

    # Button to trigger prediction
    if st.button("Predict Rent"):
        # Predict the rent
        rent = predict_rent(location, total_sqft, bhk, bath)
        st.write(f"The predicted rent for the given details is: ₹ {rent:,.2f} per month")

if __name__ == "__main__":
    main()