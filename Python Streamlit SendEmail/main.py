import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')


col1, empty_col1, col2 = st.columns([2.0, 0.1, 4.0])

# Column 1:
with col1:
    st.image("images1/image1.jpg", width=300)

# Column 2:
with col2:
    st.title("Code 123")
    content = """Hello I am Code, I am a Python Programmer 
    I also like to do other UIUX Design and Prototyping,
    feel free to get back to me if you would like to hire someone
    to build great app. Feel free to reach out to me, I would like
    to build great application and know the different python programming coding"""
    st.write(content)

content2 = """Reach out to me if you would like to connect,
my email is abc@hotmail.com and my number is 12345678, I would 
like to build great project and also understand the different concept of programming."""
st.info(content2)

# Ratio Dimension of the Columns, the content is responsive for mobile device
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        # Using the f-string here
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]}')

# Run this file in Streamlit using streamlit run main.py
# Need to Download and Install the streamlit library
