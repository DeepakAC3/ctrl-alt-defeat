import streamlit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


age = streamlit.number_input("Enter your age:")
smoke = streamlit.radio("If you smoke", ("Yes", "No"))
chronic = streamlit.radio("If you have chronic disease", ("Yes", "No"))
wheezing = streamlit.radio("If you have wheezing", ("Yes", "No"))
alcohol = streamlit.radio("If you drink alcohol", ("Yes", "No"))
coughing = streamlit.radio("If you have coughing", ("Yes", "No"))
shortness_of_breath = streamlit.radio("If you have shortness of breath", ("Yes", "No"))
swallowing_difficulty = streamlit.radio("If you have swallowing difficulty", ("Yes", "No"))
chest_pain = streamlit.radio("If you have chest pain", ("Yes", "No"))

submit_button = streamlit.button("Submit")


if smoke == "Yes":
    smoke = 1
else:
    smoke = 0

if chronic == "Yes":
    chronic = 2
else:
    chronic = 1

if wheezing == "Yes":
    wheezing = 2
else:
    wheezing = 1

if alcohol == "Yes":
    alcohol = 2
else:
    alcohol = 1

if coughing == "Yes":
    coughing = 2
else:
    coughing = 1

if shortness_of_breath == "Yes":
    shortness_of_breath = 2
else:
    shortness_of_breath = 1

if swallowing_difficulty == "Yes":
    swallowing_difficulty = 2
else:
    swallowing_difficulty = 1

if chest_pain == "Yes":
    chest_pain = 2
else:
    chest_pain = 1



if submit_button:
    streamlit.write("Age: ", age)
    streamlit.write("Smoke: ", smoke)
    streamlit.write("Chronic: ", chronic)
    streamlit.write("Wheezing: ", wheezing)
    streamlit.write("Alcohol: ", alcohol)
    streamlit.write("Coughing: ", coughing)
    streamlit.write("Shortness of breath: ", shortness_of_breath)
    streamlit.write("Swallowing difficulty: ", swallowing_difficulty)
    streamlit.write("Chest pain: ", chest_pain)
# Path: Hackathon/app.py