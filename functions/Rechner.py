from datetime import datetime
import streamlit as st
import pandas as pd
import pytz
def berechne_bmi(gewicht, groesse, einheit='m', klassifizieren=False):
    """
    Berechnet den Body-Mass-Index (BMI).
    Parameter:
      gewicht    : Zahl (kg)
      groesse    : Zahl (Meter oder Zentimeter, je nach 'einheit')
      einheit    : 'm' für Meter (Standard) oder 'cm' für Zentimeter
      klassifizieren: bool, wenn True wird zusätzlich eine Kategorie zurückgegeben
    Rückgabe:
      float BMI oder (BMI, Kategorie) wenn klassifizieren=True
    Raises:
      TypeError, ValueError
    """
    if not isinstance(gewicht, (int, float)) or not isinstance(groesse, (int, float)):
        raise TypeError("gewicht und groesse müssen Zahlen (int oder float) sein")

    if einheit == 'cm':
        groesse_m = groesse / 100.0
    elif einheit == 'm':
        groesse_m = groesse
    else:
        raise ValueError("einheit muss 'm' oder 'cm' sein")

    if groesse_m <= 0 or gewicht <= 0:
        raise ValueError("gewicht und groesse müssen größer als 0 sein")

    bmi = gewicht / (groesse_m ** 2)

    if klassifizieren:
        if bmi < 18.5:
            kategorie = "Untergewicht"
        elif bmi < 25:
            kategorie = "Normalgewicht"
        elif bmi < 30:
            kategorie = "Übergewicht"
        else:
            kategorie = "Adipositas"

        return {
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),  # Current swiss time
        "height": groesse_m,
        "weight": gewicht,
        "bmi": round(bmi, 1),
        "category": kategorie }
    
   


 
