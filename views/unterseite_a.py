import streamlit as st
from functions.Rechner import berechne_bmi
st.title("BMI Rechner")

st.write("Diese Seite ist eine Unterseite der Startseite.")


with st.form("my_form"):
    st.write("Inside the form")
    Height = st.number_input("Insert a height")
    Weight = st.number_input("Insert a weight")
    checkbox_val = st.checkbox("My weight and height are accurate")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        if Height <= 0 or Weight <= 0:
            st.warning('weight and height must be greater than 0', icon="⚠️")
        else: 
            st.write(berechne_bmi(Weight, Height, klassifizieren=True))
st.write("Outside the form")