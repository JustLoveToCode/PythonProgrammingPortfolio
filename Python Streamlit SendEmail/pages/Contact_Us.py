import streamlit as st
from send_email import send_email

st.header('Contact Us for more Information')

with st.form(key='email_forms'):
    user_email = st.text_input("Your Email Address")
    phone = st.text_input('Your Phone Number')
    raw_message = st.text_area('Input your Message Here')
    # This is the message received on the email address
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
{phone}
"""
    button = st.form_submit_button('Submit Here')

    if button:
        send_email(message)
        st.info("Your email was sent successfully")
