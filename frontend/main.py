import requests
import streamlit as st
from PIL import Image
from styles import STYLES

# st.set_option("deprecation.showfileUploaderEncoding", False)

# define a h1 header
st.title("Style transfer using neural style transfer")

# displays a file uploader
img = st.file_uploader("Choose an Image")

# display the selection for styles
style = st.selectbox("Choose a style", [s for s in STYLES.keys()])

# displays a button
if st.button("Style Transfer"):
    if img is not None and style is not None:
        files = {"file": img.getvalue()}
        res = requests.post(f"http://backend:8080/{style}", files=files)
        img_path = res.json()
        image = Image.open(img_path[0])
        col1, col2 = st.columns(2)
        col1.image(img)
        col1.write("Orignal Image")
        col2.image(image)
        col2.write("Style Transeferred Image")
        # st.image(image, width=500)
