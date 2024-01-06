import streamlit as st
import pandas as pd

# Set the Website Page Configuration from Default Centered to Wide
# to fill the Entire Website Page
st.set_page_config(layout="wide")

# Add the header and some other text:
st.header('The Best Company to Be')

st.write("""This is the best company that you can be with, it has the best welfare
for their employees and able to take care of the employee need and wants, the
manager is always supportive of the subordinate decision and the leadership
management is very strong. Also, there is free pantries where you can eat all you want
and also able to bring home the food that it is needed.""")

st.subheader('Our Team of Leadership')

# This line will create the columns here where it is 3 different columns
col1, col2, col3, col4 = st.columns(4)

# Make the dataframe with the company members with the Database
df = pd.read_csv('data.csv')

# Add content to the first column
with col1:
    # Iterate from row 0 to row 2 with row 3 exclusive:
    for index, row in df[:3].iterrows():
        # Add the members first and the last names
        st.subheader(f"{row['first name'].title()} {row['last name']}")
        # Add the member roles in the company
        st.write(row["role"])
        # Add member photos by accessing the images folder
        # using the "images/" directory
        st.image("images/" + row["image"])

with col2:
    # Iterate from row 3 to 5 with row 6 exclusive:
    for index, row in df[3:6].iterrows():
        # Add the member first and the last names
        st.subheader(f"{row['first name'].title()} {row['last name']}")
        # Add the member roles in the company
        st.write(row["role"])
        # Add member photos by accessing the images folder
        # using the "images/" directory
        st.image("images/" + row["image"])


with col3:
    # Iterate from row 6 to row 8 with row 9 exclusive
    for index, row in df[6:9].iterrows():
        # Adding the member first and the last names
        st.subheader(f"{row['first name'].title()} {row['last name']}")
        # Add the member roles in the company
        st.write(row['role'])
        # Adding the member photos by accessing the images folder
        # using the "images/" directory
        st.image("images/" + row["image"])


with col4:
    # Iterate from row 9 to row 11 with row 12 exclusive:
    for index,row in df[9:12].iterrows():
        # Adding the member first and the last names:
        st.subheader(f"{row['first name'].title()}{row['last name']}")
        # Add the member roles in the company
        st.write(row['role'])
        # Adding the member photo by accessing the images folder
        # using the "images/" directory
        st.image("images/"+ row["image"])




