import streamlit as st

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