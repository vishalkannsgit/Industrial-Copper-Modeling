import streamlit as st
import numpy as np
import joblib  # To load saved models

# Load your models
price_model = joblib.load('price_model.pkl')  # Change to your model file name
status_model = joblib.load('status_model.pkl')  # Change to your model file name

# Title of the app
st.title("Price and Status Prediction App")

# Input fields for the features
st.header("Input Features")
feature_1 = st.number_input("Feature 1")
feature_2 = st.number_input("Feature 2")
# Add more input fields as required based on your features

# Button for prediction
if st.button("Predict"):
    # Prepare the input data for the model
    input_data = np.array([[feature_1, feature_2]])  # Update with actual feature names
    predicted_price = price_model.predict(input_data)
    predicted_status = status_model.predict(input_data)

    # Display the predictions
    st.write(f"Predicted Price: ${predicted_price[0]:.2f}")
    st.write(f"Predicted Status: {predicted_status[0]}")
