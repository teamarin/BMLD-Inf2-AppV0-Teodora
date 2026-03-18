import streamlit as st
from functions.Rechner import berechne_bmi
import pandas as pd
from utils.data_manager import DataManager  

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
            results = berechne_bmi(Weight, Height, klassifizieren=True)
            
            st.write("Outside the form")
            st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([results])], ignore_index=True)
            # --- CODE UPDATE: save data to data manager ---
            data_manager = DataManager()
            data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
    # --- END OF CODE UPDATE ---
# --- NEW CODE to display the history table ---
st.dataframe(st.session_state['data_df'])

# Beispiele:
# berechne_bmi(70, 1.75) -> ~22.86
# berechne_bmi(70, 175, einheit='cm', klassifizieren=True) -> (22.86..., 'Normalgewicht')
# ...existing code...
