import streamlit as st
import pandas as pd
import joblib

model = joblib.load("logistic_regression_student_study_model.pkl")

st.title("Student Pass / Fail Based on Study Hours")
hours = st.number_input("Enter the study hours" , min_value =0.0 ,max_value = 15.0 ,value=5.0)
attendance = st.number_input("Enter the attendance" , min_value =0.0 ,max_value = 100.0,value=75.0)


if st.button("Predict"):
  # input_data = pd.DataFrame(
  prediction = model.predict([["StudyHours","Attendance"]])
  probability = model.predict_proba([["StudyHours","Attendance"]])
  if prediction[0] == 1:
    st.success("Pass")
  else:
    st.error("Fail")
  pass_probability = probability[0][1]
  st.write("Pass probability : ",pass_probability*100,"%")
