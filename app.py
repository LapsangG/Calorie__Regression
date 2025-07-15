import streamlit as st
import numpy as np
import pickle

# Loading my saved Linear Regression model
with open("linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit App Title
st.title(" Calories Burned Prediction App")

st.write("""
Enter your workout and personal details below to predict the estimated calories burned using a machine learning model trained on exercise data.
""")

# Gender input — note: 1 = Male, 0 = Female
gender = st.selectbox("Select Gender", options=["Male", "Female"])
gender_encoded = 1 if gender == "Male" else 0

# Other inputs based on my dataset
age = st.slider("Age", 10, 80, 25)
height = st.slider("Height (cm)", 100, 250, 170)
weight = st.slider("Weight (kg)", 30, 200, 65)
duration = st.slider("Duration of Exercise (minutes)", 1, 300, 30)
heart_rate = st.slider("Average Heart Rate (bpm)", 60, 200, 100)
body_temp = st.slider("Body Temperature (°C)", 30.0, 45.0, 37.0)

# Arranging inputs in the order used in my model:
# ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
input_data = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])

# Predicting
if st.button("Predict Calories Burned"):
    prediction = model.predict(input_data)
    st.success(f"🔥 Estimated Calories Burned: **{prediction[0]:.2f}** calories")
