import streamlit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


age = streamlit.text_input("Enter your age:")
smoke = streamlit.text_input("Enter 1 if you smoke, 0 if you don't:")
chronic = streamlit.text_input("Enter 1 if you have a chronic disease, 2 if you don't:")
wheezing = streamlit.text_input("Enter 1 if you have wheezing, 2 if you don't:")
alcohol = streamlit.text_input("Enter 1 if you drink alcohol, 2 if you don't:")
coughing = streamlit.text_input("Enter 1 if you have coughing, 2 if you don't:")
shortness_of_breath = streamlit.text_input("Enter 1 if you have shortness of breath, 2 if you don't:")
swallowing_difficulty = streamlit.text_input("Enter 1 if you have swallowing difficulty, 2 if you don't:")
chest_pain = streamlit.text_input("Enter 1 if you have chest pain, 2 if you don't:")


# Path: Hackathon/app.py