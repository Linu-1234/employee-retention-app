import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit app interface
st.title("🚀 Employee Attrition Predictor")
st.write("Enter employee details to predict if they are likely to leave the company.")

# Collect user inputs
satisfaction = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
monthly_hours = st.slider("Average Monthly Hours", 80, 310, 160)
promotion = st.selectbox("Promotion in Last 5 Years", [0, 1])
time_spent = st.slider("Years at Company", 1, 10, 3)
salary = st.selectbox("Salary Level", ["low", "medium", "high"])

# Convert salary to dummy variables (as in training)
low = medium = 0
if salary == "low":
    low = 1
elif salary == "medium":
    medium = 1

# Feature array (excluding 'high' due to dummy variable trap)
features = np.array([[satisfaction, monthly_hours, promotion, time_spent, low, medium]])

# Prediction button
if st.button("Predict Attrition"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ This employee is likely to leave.")
    else:
        st.success("✅ This employee is likely to stay.")