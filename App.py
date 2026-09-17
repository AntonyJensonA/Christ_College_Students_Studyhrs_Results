import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Price_Model.pkl")

st.title("House Price Prediction")
area = st.number_input("Enter the area in sq_ft" , min_value = 600.00 ,max_value = 3000.0 ,value=610.0)
bedroom = st.number_input("Enter the number of bedrooms" , min_value =1.0 ,max_value = 4.0,value=2.0)
floor = st.number_input("Enter the number of bedrooms" , min_value = 0.0 ,max_value = 10.0,value=2.0)

if st.button("Predict"):
  if area < 600 or area > 3000: 
    st.error("Area should be between 600 and 3000 sq ft")     
  elif bedroom < 1 or bedroom > 4: 
    st.error("Number of bedrooms should be between 1 and 4") 
  elif floor < 0 or floor > 10: 
    st.error("Floor number should be between 0 and 10") 
  else:
    input_data = pd.DataFrame({ "Area": [area], "Bedrooms": [bedroom], "Floor": [floor] }) 
    prediction = model.predict(input_data) 
    pred = prediction[0] 
    st.success(f"Predicted Price: ₹{pred:.2f} Lakhs")
