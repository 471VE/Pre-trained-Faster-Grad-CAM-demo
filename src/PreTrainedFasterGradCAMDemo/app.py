import numpy as np
import streamlit as st
from PIL import Image

from PreTrainedFasterGradCAMDemo import demo

st.set_page_config(layout="wide")
st.title("Faster Grad-CAM demo")
st.write(
    "This web app uses model that predicts whether "
    "the hand on a given image is open or closed. "
    "It also produces a heatmap of important regions "
    "on an image that contribute the most to the "
    "final prediction of the model using Grad-CAM approach.\n\n"
    "Original model can be found here: "
    "https://github.com/shinmura0/Faster-Grad-CAM\n\n"
    "Model weights were taken from here: "
    "https://github.com/PINTO0309/PINTO_model_zoo/tree/main/015_Faster-Grad-CAM"
)

uploaded_file = st.file_uploader("Upload your image of the hand here", type=["png", "jpg", "jpeg"])
col1, col2, col3 = st.columns(3)

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    col1.image(img, "Original image")

    hand_positions, processed_images = demo.main([np.array(img)], False)
    if hand_positions[0] == "Closed":
        col2.image(processed_images[0][0], "Heatmap of Grad-CAM")
        col3.image(processed_images[0][1], "Position of the closed hand")
    else:
        col2.image(processed_images[0][1], "No closed hand detected")
