import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.set_page_config(page_title="Urdu OCR - Code Saviours SI-26", page_icon="📝")
st.title("Urdu OCR — Code Saviours SI-26")
st.write("Upload an image containing Urdu text and get the extracted text.")

@st.cache_resource
def load_reader():
    reader = easyocr.Reader(['ur'])   # 'ur' = Urdu language code
    return reader

reader = load_reader()

uploaded_file = st.file_uploader("Upload Urdu Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Urdu Image")

    if st.button("Extract Urdu Text"):
        result = reader.readtext(np.array(image), detail=0, paragraph=True)
        text = " ".join(result)

        if text:
            st.subheader("Extracted Urdu Text")
            st.write(text)
        else:
            st.write("?????.")
