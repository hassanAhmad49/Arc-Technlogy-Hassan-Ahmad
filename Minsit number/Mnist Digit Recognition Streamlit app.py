import joblib
import numpy as np
import streamlit as st
from PIL import Image
import cv2

# Load models + scaler
log_reg = joblib.load("logistic_model.pkl")
svm_model = joblib.load("svm_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("MNIST Digit Recognition 🖊️")
st.write("Upload a handwritten digit image (28x28, black & white).")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Read & preprocess
    image = Image.open(uploaded_file).convert("L")  # grayscale
    img_resized = image.resize((28, 28))
    img_array = np.array(img_resized)

    st.image(img_resized, caption="Uploaded Digit", use_container_width=True)

    # Flatten + scale
    img_flat = img_array.flatten().reshape(1, -1)
    img_scaled = scaler.transform(img_flat)  # ✅ now works

    # Predict
    log_pred = log_reg.predict(img_scaled)[0]
    svm_pred = svm_model.predict(img_scaled)[0]

    st.subheader("🔮 Predictions")
    st.write(f"**Logistic Regression:** {log_pred}")
   
