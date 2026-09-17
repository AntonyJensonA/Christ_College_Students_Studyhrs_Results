import streamlit as st
import joblib

model = joblib.load("logistic_regression_student_study_model.pkl")

st.title("Student Pass / Fail Based on Study Hours")
hours = st.number_input("Enter the study hours" , min_value =0.0 ,max_value = 15.0 ,value=5.0)

if st.button("Predict"):
  prediction = model.predict([[hours]])
  probablity = model.predict_proba([[hours]])
  if prediction[0] == 1:
    st.success("Pass")
  else:
    st.error("Fail")
  print("Probabiliy : ",probability)
