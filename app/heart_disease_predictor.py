# Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

import os

print(os.getcwd())
os.chdir("/Users/mani/Desktop/heart-disease-predictor/app")
print(os.getcwd())

# Linking the CSS file
def local_css(filename):
    with open(filename) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Sidebar
st.sidebar.title("Input Descriptions")
st.sidebar.markdown(
    "Resting ECG: common procedure used by doctors to check for signs of heart disease. Below are the corresponding numbers and what they mean."
    )
st.sidebar.markdown("* 0 - Normal")
st.sidebar.markdown("* 1 - ST-T wave abnormality")
st.sidebar.markdown("* 2 - Probable or definite left ventricular hypertrophy")



# Title and project description
st.title("Heart Disease Predictor")
st.write("Using the Heart Disease Dataset from the University of California Irvine Machine Learning Repository, we trained a logistic regression model that predicts the probability of an individual having heart disease. Below are the respective attributes that were used when training the model.")

# Directions
st.subheader("Directions:")
st.write("Fill in the input fields below to get a prediction")

# Age input
age = st.number_input(label="Enter your age:", value=0)

# Sex input
sex =  st.selectbox(label="Select your sex:", options=['',"Male", "Female"], format_func=lambda x: 'Select an option' if x == '' else x)
# Mapping sex to 1 or 0
if sex == 'Male':
    sex = 1
else:
    sex = 0

# Fbs input
fbs = st.selectbox('Is your fasting blood sugar above 120 mg/dl?', ['', 'Yes', 'No'], format_func=lambda x: 'Select an option' if x == '' else x)
# Mapping fbs to the appropriate value
if fbs == 'Yes':
    fbs = 1
else:
    fbs = 0


# Ecg input
ecg = st.radio(label="What is your resting ECG value(Please refer to the side bar for explanations on what each value represents)?", options=[0, 1, 2])

# Thalach input
thalach = st.number_input(label="Enter your maximum heart rate(bpm):", value=0)

# Exang input
exang = st.selectbox('Do you experience chest pain when exercising?', ['', 'Yes', 'No'], format_func=lambda x: 'Select an option' if x == '' else x)
# Mapping exang to the appropriate value
if exang == 'Yes':
    exang = 1
else:
    exang = 0
    
# Oldpeak input
oldpeak = st.number_input(label="What is your st depression value induced by exercise relative to rest?")

# Chest pain input
cp = st.selectbox('Do you have chest pain? If so, which option best describes your chest pain?', ['', 'No chest pain', 'Typical angina', 'Atypical angina', 'Non-anginal pain'], format_func=lambda x: 'Select an option' if x == '' else x)
if cp == 'Typical angina':
    cp = 1
elif cp == 'Atypical angina':
    cp = 2
elif cp == 'Non-anginal pain':
    cp = 3
elif cp == 'No chest pain':
    cp = 4

# Ca input
ca = st.radio(label='How many major arteries do you have blocked(stained with fluoroscopy)?', options=[0, 1, 2, 3])

# Thal input
thal = st.selectbox('Do you have thalassaemia? If so, is it reversible or a fixed defect?', ['', 'I do not have thalassaemia', 'Reversible', 'Fixed defect'], format_func=lambda x: 'Select an option' if x == '' else x)
if thal == 'I do not have thalassaemia':
    thal = 3
elif thal == 'Fixed defect':
    thal = 6
elif thal == 'Reversible':
    thal = 7

# Creating a function that will train the model and cache it

@st.cache 
def train_model():
    """
    Trains the logistic regression model and caches it
    return: A trained logistic regression model
    """
    # Importing the Cleveland data
    df_cleveland = pd.read_csv("/Users/mani/Desktop/heart-disease-predictor/data/cleveland_data.csv", index_col=0)
    
    # Removing the unnecessary features
    df_cleveland.drop(['trest', 'chol', 'slope'], axis=1, inplace=True)
    
    # Separting the data into features and labels
    X = df_cleveland.loc[:, df_cleveland.columns != "num"]
    y = df_cleveland["num"]
    
    # Creating a logistic regression model
    lr_classifier = LogisticRegression(tol=1e-6, solver='liblinear', max_iter=200,)
    
    # Training the model
    lr_classifier.fit(X, y)
    
    # Return the model
    
    return lr_classifier

model = train_model()

# Putting the user input in an array to pass to the predict function
input = [[
    age,
    sex,
    cp,
    fbs,
    ecg,
    thalach,
    exang,
    oldpeak,
    ca,
    thal
]]

# Only getting a prediction if all inputs fields have been completed

# Counter that keeps track of the number of completed input fields
is_empty = 0
for inner in input:
    for value in inner:
        if value != '':
            is_empty += 1
            #st.write(is_empty)



#st.write(input)

# Button for form submission
button = st.button(label='Submit')

# Getting a prediction from the model based on the user input
if is_empty == 10 and button:
    prediction = model.predict_proba(input)
    proba = 100 * round(prediction[0][1], 2)
    proba = str(proba)
    
    st.write("The probability of having heart disease is " + proba + "%")
elif is_empty != 10 and button:
    st.write("Error: Please make sure all the input fields are filled in.")
    

