import streamlit as st
from PIL import Image

st.title('GrayScale Generator')
st.subheader('Color to GrayScale Generator')

# Creating the file uploader component allowing the user
# to upload the file
uploaded_image = st.file_uploader('UPLOAD Image here')

# Create the Expander Component in Camera
with st.expander('START Camera'):
    # We start the camera here
    # We get the None Attribute when we first started the Camera
    # Reason is because when we first start the camera, it ask for
    # permission from the user to use the Camera, However, Python
    # script is still running and hence, it return the NoneType Attribute.
    camera_image = st.camera_input('Camera')

# If there is camera_image, this conditional code will run
if camera_image:
    # Create pillow image instance
    img = Image.open(camera_image)
    # PIL has the method of convert
    # Convert the pillow image to Gray Scale
    gray_camera_img = img.convert("L")

    # Render the GrayScale image on the Webpage
    st.image(gray_camera_img)

# Check if the image existed, if the user have uploaded the file
if uploaded_image:

    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to GrayScale
    gray_uploaded_img = img.convert("L")
    # Display the grayscale image on the webpage
    # If this code is not created, the image will not get uploaded to the webpage
    st.image(gray_uploaded_img)


