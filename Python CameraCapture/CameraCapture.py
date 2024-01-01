import streamlit as st
from PIL import Image

# Create the Expander Component in Camera
with st.expander('Start Camera'):
    # We start the camera here
    # We get the None Attribute when we first started the Camera
    # Reason is because when we first start the camera, it ask for
    # permission from the user to use the Camera, However, Python
    # script is still running and hence, it return the NoneType Attribute.
    camera_image = st.camera_input('Camera')


if camera_image:
    # Create pillow image instance
    img = Image.open(camera_image)
    # PIL has the method of convert
    # Convert the pillow image to Gray Scale
    gray_img = img.convert("L")

    # Render the GrayScale image on the Webpage
    st.image(gray_img)

uploaded_image = st.file_uploader('Upload Image')
