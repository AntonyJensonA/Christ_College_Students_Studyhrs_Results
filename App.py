import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Price_Model.pkl")

st.title("House Price Prediction")
area = st.number_input("Enter the area in sq_ft" , min_value = 600.00 ,max_value = 3000.0 ,value=610.0)
if area <600.00 or area>3000.00:
  st.error("Area should be between 600 and 3000 sq ft")
bedroom = st.number_input("Enter the number of bedrooms" , min_value =1.0 ,max_value = 4.0,value=2.0)
if bedroom <1.0 or bedroom>4.0:
  st.error("No of bedrooms should be between 1 and 10")
floor = st.number_input("Enter the number of bedrooms" , min_value = 0.0 ,max_value = 10.0,value=2.0)
if floor <1.0 or floor>10.0:
  st.error("No of floors should be between 1 and 10")

input_data = pd.DataFrame({
  "Area":[area],
  "Bedrooms":[bedroom],
  "Floor":[floor]
})

if st.button("Predict"):
  prediction = model.predict(input_data)
  pred = prediction[0]
  st.success(f"Predicted Price: ₹{pred:.2f} Lakhs")
