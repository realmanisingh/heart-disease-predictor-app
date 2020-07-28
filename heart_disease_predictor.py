# Importing libraries
import streamlit as st

# Title and project description
st.title("Heart Disease Predictor")
st.write("Using the Heart Disease Dataset from the University of California Irvine Machine Learning Repository, we trained a logistic regression model that predicts the probability of an individual having heart disease. Below are the respective attributes that were used when training the model.")

# Directions
st.subheader("Directions:")
st.write("Fill in the input fields below to get a prediction")

# Age input
age = st.number_input(label="Enter your age", value=0)
st.write("The age is", age)

# Sex input
sex =  st.selectbox(label="Select your sex", options=['',"Male", "Female"], format_func=lambda x: 'Select an option' if x == '' else x)
st.write("The sex is", sex)

# Fbs input
fbs = st.selectbox('Is your fasting blood sugar above 120 mg/dl?', ['', 'Yes', 'No'], format_func=lambda x: 'Select an option' if x == '' else x)
st.write("The fbs is", fbs)

# Ecg input
ecg = st.radio(label="What is your resting ECG value(Please refer to the side bar for explanations on what each value represents)", options=[0, 1, 2])
st.write("The ecg is", ecg)

# Thal input
thalach = st.number_input(label="Enter your maximum heart rate(bpm)", value=0)
st.write("The thalach is", thalach)

# Exang input
exang = st.selectbox('Do you experience chest pain when exercising?', ['', 'Yes', 'No'], format_func=lambda x: 'Select an option' if x == '' else x)
st.write("The exang is", exang)

# Oldpeak input
oldpeak = st.number_input(label="What is your st depression value induced by exercise relative to rest")
st.write("The oldpeak is", oldpeak)