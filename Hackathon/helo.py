import streamlit as st
from PIL import Image

#title
st.title("Hello World")

#header
st.header("Hello Header")

#subheader
st.subheader("Hello Subheader")

#text
st.text("Hello Text")

#success,info
st.success("Executed Successfully")
st.info("Information")
st.warning("This is a warning")
st.error("Error was encountered")

#write
st.write("I'm writing this sample code")
st.write(range(20))
channel = "Ghost_Dragon"
st.write("Add me as a friend on discord: ",channel)

#code
code_body = '''for i in range(10):
    print(i)'''
st.code(code_body, language = "python")

#checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

#radio
status = st.radio("What is your status", ("Active", "Inactive"))
st.write("Your status is: ", status)

#image
img = Image.open("Hackathon/obama pog.png")
st.image(img, width = 300, caption = "Obama Pog")

#selection box
option = st.selectbox("Select an option", ['python','java','c++'])
st.write("You selected: ", option)

#multiselect
options = st.multiselect("Select multiple options", ['python','java','c++'])
st.write("You selected: ", options)
