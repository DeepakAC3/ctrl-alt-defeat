import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hello",
    page_icon="👋"
)
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

components.html("""<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<style>
  body, html {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    background: url('/c:/codeStuffs/Finance/test/bgimage.png') no-repeat center center fixed;
    background-size: cover;
    font-family: Arial, sans-serif;
    background-color: rgba(0, 0, 0, 0.6); /* Reduced opacity of the background */
}

img {
    opacity: 0.9;
    width: 220px;
    margin-left: 100px;
}

.navbar {
    width: 100%;
    height: 50px;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    box-sizing: border-box;
}

.navbar-links {
    display: flex;
}

.navbar a {
    color: #e6ebe2;
    text-decoration: none;
    font-family: cursive;
    margin-left: 15px;
    font-size: 22px;
    padding: 5px 13px;
    border: 2px solid white;
    border-radius: 20px;
    transition: background-color 0.3s, color 0.3s; /* Add transition for hover effects */
}

.navbar a:hover {
    background-color: white;
    color: #08509f;
}

.brand-title {
    color: white;
    font-size: 32px;
    font-family: 'Open Sans', sans-serif;
    text-shadow: 2px 2px 4px #000000;
}

h1 {
    font-family: 'Open Sans', sans-serif;
    color: #dfddce;
    text-align: center;
    font-size: 44px;
    text-shadow: 2px 2px 4px #000000;
}

.main-content {
    text-align: left;
    width: 40%;
    background-color: rgba(37, 62, 78, 0.8); /* Adjusted background opacity */
    padding: 30px;
    margin-top: 100px;
    position: absolute;
    top: 30%;
    left: 4%;
    transform: translateY(-40%);
    color: white;
    border-radius: 25px;
    overflow: hidden;
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5); /* Added shadow effect */
}

.main-content p {
    font-size: 24px;
    margin: 0;
    white-space: pre-wrap;
    overflow: hidden;
}

/* Additional global styles */
a, p, h1 {
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7); /* Subtle text shadow for all text */
}

</style>
<body>
  <div class="navbar">
    <div class="brand-title"><img src="/c:/codeStuffs/Finance/test/image.png" height = "50px" width = "170px"></div>
    <div class="navbar-links">
      <a href="#home"><b>HOME</b></a>
      <a href="#about-us"><B>ABOUT US</B></a>
      <a href="#login"><b>LOGIN</b></a>
    </div>
  </div>
  <div class="main-content">
    <h1>IQ FINANCE</h1>
    <p>
        Our website provides users with a powerful set of financial management tools to take control of their finances effectively. From intuitive expense tracking and categorization features to insightful visualizations and budget tracking capabilities, users can easily monitor their spending habits and make informed decisions. Additionally, our platform leverages advanced prediction models like ARIMA for forecasting future expenses and offers credit score assessment through binary classification models. With our comprehensive suite of tools and services, users can confidently manage their finances, improve financial health, and plan for a secure financial future.  
    </p>
  </div>
</body>
</html>
""",width=1000, height=1000)
st.sidebar.header("Select a demo above.")

# st.write("# Welcome to streamlit! 👋")

# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )