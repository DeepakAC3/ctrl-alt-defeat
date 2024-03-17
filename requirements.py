import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import seaborn as sns
import matplotlib as plt


print(np.__version__)
print(pd.__version__)
print(joblib.__version__)
print(sns.__version__)
print(plt.__version__)

# scikit-learn = 1.4.1.post1
# matplotlib = 3.7.1
# seaborn = 0.13.0
# numpy = 1.26.0
# pandas = 1.5.1
# joblib = 1.3.2
# flask = 3.0.2
# langchain_openai = 0.0.6
# langchain_core = 0.0.6
# langchain_core = 0.1.24
