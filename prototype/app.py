import streamlit as st

st.title("AI Blog Generator")

keyword = st.text_input("Enter a keyword")

if st.button("Generate Blog"):
    st.write("Generating blog for:", keyword)
    st.write("This is a sample blog output based on the keyword.")