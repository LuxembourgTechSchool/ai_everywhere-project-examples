import os
import streamlit as st
from proxy import lts_proxy

proxy = lts_proxy.Proxy()

st.title("OpenAI Vision API Example: Menu Extractor")

system_message = st.text_area("Enter instructions for the vision model:", 
                              "Extract all menu items and translate them into English.")

# Example file: files/menu-hindi.jpg
uploaded_file = st.file_uploader("Upload a menu image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file and system_message:
    temp_image_path = f"temp_{uploaded_file.name}"
    with open(temp_image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try: 
        with st.spinner("Processing image..."):
            response = proxy.get_vision(temp_image_path, system_message)

        if response:
            st.subheader("Extracted Menu Items:")
            st.write(response)
        else:       
            st.error("Failed to process the image. Please try again.")
    finally:
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)
