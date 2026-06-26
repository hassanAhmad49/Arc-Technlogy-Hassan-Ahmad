# 1. Import necessary libraries
# -----------------------------
import streamlit as st
import numpy as np
import joblib
import os

# 2. Set the page title and layout
# --------------------------------
st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸",
    layout="centered"
)

# 3. Application header and description
# -------------------------------------
st.title("🌸 Iris Flower Species Classifier")
st.write(
    "This app uses a pre-trained K-Nearest Neighbors (KNN) model to predict the species of an "
    "Iris flower. Please enter the measurements below to get a prediction."
)
st.write("---")

# 4. Load the pre-trained model
# -----------------------------
# We'll use the joblib file as it's the recommended format for scikit-learn models.
model_filename = 'iris_knn_model.joblib'

# Check if the model file exists before trying to load it
if not os.path.exists(model_filename):
    st.error(f"Error: Model file '{model_filename}' not found. "
             "Please make sure the file is in the same directory as this script.")
    st.stop()
else:
    try:
        model = joblib.load(model_filename)
    except Exception as e:
        st.error(f"Failed to load the model. Please check the file. Error: {e}")
        st.stop()

# Define the target species names for clear output
species_names = ['setosa', 'versicolor', 'virginica']

# 5. Create input widgets for user data
# -------------------------------------
st.header("Enter Flower Measurements")

# Create a container for the input sliders
with st.container(border=True):
    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=4.0, max_value=8.0, value=5.1, step=0.1
    )
    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=2.0, max_value=4.5, value=3.5, step=0.1
    )
    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=1.0, max_value=7.0, value=1.4, step=0.1
    )
    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.1, max_value=2.5, value=0.2, step=0.1
    )

# 6. Prediction button and logic
# ------------------------------
if st.button("Predict Species"):
    # Create a numpy array from the user inputs
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make the prediction using the loaded model
    prediction_index = model.predict(input_data)[0]
    predicted_species = species_names[prediction_index]

    # 7. Display the prediction result
    # --------------------------------
    st.write("---")
    st.header("Prediction Result")
    
    # Use different messages based on the prediction
    if predicted_species == 'setosa':
        st.success(f"Based on the measurements, the Iris flower is **Setosa** 🌿.")
        st.info("Setosa flowers are known for their short and narrow petals.")
    elif predicted_species == 'versicolor':
        st.success(f"Based on the measurements, the Iris flower is **Versicolor** 🌺.")
        st.info("Versicolor flowers have mid-range petal and sepal sizes.")
    else:
        st.success(f"Based on the measurements, the Iris flower is **Virginica** 🌷.")
        st.info("Virginica flowers typically have the longest and widest petals.")

    st.balloons()
