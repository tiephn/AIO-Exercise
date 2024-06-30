import streamlit as st

st.title('Object Detection for images')
file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
if file is not None:
    st.image(file, caption="Uploaded Image")
