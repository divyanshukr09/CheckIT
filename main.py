# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:28:49 2023

@author: kritika singh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    with col1:
        cp = st.text_input('Chest Pain types')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        exang = st.text_input('Exercise Induced Angina')

    with col2:
        age = st.text_input('Age')

    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[chol, thalach, thal, cp, oldpeak, ca, exang, age, slope]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        PPE = st.text_input('PPE')
    with col2:
        spread1 = st.text_input('spread1')

    with col3:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col4:
        spread2 = st.text_input('spread2')
    with col5:
        APQ = st.text_input('MDVP:APQ')
    with col1:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col4:
        HNR = st.text_input('HNR')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        PPQ = st.text_input('MDVP:PPQ')

    with col2:
        RAP = st.text_input('MDVP:RAP')
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[PPE, spread1, fo, spread2, APQ, flo, Jitter_Abs, fhi, HNR,
                                                           NHR, Jitter_percent, APQ5, APQ3, DDA, Shimmer_dB, PPQ, RAP,
                                                           Shimmer]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
