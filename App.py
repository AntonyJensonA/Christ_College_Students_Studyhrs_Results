import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Price_Model.pkl")
st.title("House Price Prediction")

area = st.number_input(
    "Enter the area in sq_ft",
    min_value=0.0,
    max_value=10000.0,
    value=610.0
)

bedroom = st.number_input(
    "Enter the number of bedrooms",
    min_value=0.0,
    max_value=20.0,
    value=2.0
)

floor = st.number_input(
    "Enter the floor number",
    min_value=0.0,
    max_value=20.0,
    value=2.0
)

if st.button("Predict"):
    valid = True
    if area < 600 or area > 3000:
        st.error("Area should be between 600 and 3000 sq ft")
        valid = False
    if bedroom < 1 or bedroom > 4:
        st.error("Number of bedrooms should be between 1 and 4")
        valid = False
    if floor < 0 or floor > 10:
        st.error("Floor number should be between 0 and 10")
        valid = False
    if valid:
        input_data = pd.DataFrame({
            "Area_Sq_Ft": [area],
            "Bedrooms": [bedroom],
            "Price_Lakhs": [floor]
        })
        prediction = model.predict(input_data)
        pred = prediction[0]
        st.success(f"Predicted Price: ₹{pred:.2f} Lakhs")
