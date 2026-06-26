import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import time

nltk.download('stopwords')

# Load trained model and vectorizer
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Preprocessing function
ps = PorterStemmer()
def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [ps.stem(word) for word in text if word not in stopwords.words('english')]
    return ' '.join(text)

# ---- Custom CSS Styling ----
st.markdown("""
<style>
/* Title */
h1 {
    color: #0B3D91;
    font-size: 50px;
    text-align: center;
    font-weight: bold;
}

/* Instructions */
p {
    font-size: 20px;
    text-align: center;
}

/* Text area */
textarea {
    font-size: 20px;
    height: 250px;
}

/* Buttons */
.stButton>button {
    background-color: #0B3D91;
    color: white;
    font-size: 18px;
    height: 50px;
    width: 220px;
    border-radius: 10px;
}

/* Button hover */
.stButton>button:hover {
    background-color: #054A91;
}
</style>
""", unsafe_allow_html=True)

# ---- App Layout ----
st.title("📧 Email Spam Classifier")
st.markdown("<p>Enter your email below to check if it's Spam or Not Spam.</p>", unsafe_allow_html=True)

# Email input
user_input = st.text_area("✉️ Enter email text here:", height=250)

# Check Spam button
if st.button("🔍 Check Spam"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Spinner animation
        with st.spinner("Checking email..."):
            time.sleep(2)  # simulate processing
            cleaned_text = preprocess(user_input)
            vectorized_input = vectorizer.transform([cleaned_text]).toarray()
            prediction = model.predict(vectorized_input)[0]

        # Output
        if prediction == 1:
            st.error("🚨 This email is Spam! Be careful! ⚠️")
            # Optional GIF/image for Spam
            st.image("https://media.giphy.com/media/3o6ZsV1I8sYY2oX2J6/giphy.gif", width=200)
        else:
            st.success("✅ This email is Not Spam! 🎈")
            st.balloons()
            # Optional snow effect
            st.snow()

# Tips Section
st.markdown("---")
st.markdown("<p style='text-align:center;'>Built by <b>Hassan Ahmad</b> | Internship Task 1 Arc Tecnology</p>", unsafe_allow_html=True)
