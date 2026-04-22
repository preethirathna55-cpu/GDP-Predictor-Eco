import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("GDP Predictor")

# Load model
model = pickle.load(open("model.pkl","rb"))

# Inputs
inflation = st.number_input("Inflation")
unemployment = st.number_input("Unemployment")
life_exp = st.number_input("Life Expectancy")
education = st.number_input("Education")
gov = st.number_input("Gov Spending")
investment = st.number_input("Investment")
trade = st.number_input("Trade")
pop = st.number_input("Population Growth")

# Prediction
if st.button("Predict"):
    data = np.array([[inflation, unemployment, life_exp, education, gov, investment, trade, pop]])
    pred = model.predict(data)
    st.success(f"GDP: {pred[0]:.2f}")
