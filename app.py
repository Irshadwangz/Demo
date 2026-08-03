import streamlit as st
import pickle
import os
import time

@st.cache_resource
def load_model():
    if not os.path.exists("house_price_model.pkl"):
        raise FileNotFoundError("Model file not found. ")
    with open("house_price_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model
if "prediction_count" not in st.session_state:
    st.session_state.prediction_count = 0

try:
    model = load_model()
except Exception as e:
    st.error(e)
    st.stop()  

area = st.number_input("Area (sq ft)",1000,5000,1500)
bedrooms = st.slider("bedrooms", 1, 10, 3)
age = st.slider("Age of the house", 0, 30, 5)

if st.button("Predict Price"):
    try:
        prediction = model.predict([[area, bedrooms, age]])
        st.success(f"Predicted Price: ${prediction[0]:,.0f}")
        st.session_state.prediction_count += 1
    except Exception as e:
        st.error("Prediction failed. Please check the input values and try again.")
        st.exception(e)
        st.info(f"Total Predictions Made: {st.session_state.prediction_count}")

if st.button("Reset Counter"):
    st.session_state.prediction_count = 0
    st.success("Prediction counter reset.")

