import streamlit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


input1 = streamlit.text_input("Enter input 1")
input2 = streamlit.text_input("Enter input 2")
input3 = streamlit.slider("Select input 3", min_value=0, max_value=10)
input4 = streamlit.slider("Select input 4", min_value=0, max_value=10)
