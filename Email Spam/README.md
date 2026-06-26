# 📧 Email Spam Classification

A machine learning project that classifies an email / SMS message as **Spam** or **Not Spam (Ham)**.
It is trained on the `spam.csv` dataset, uses **TF-IDF** features with a scikit-learn classifier, and is served through an interactive **Streamlit** web app.

> Internship Task 1 — Arc Technologies · Built by **Hassan Ahmad**

---

## 🧠 How It Works (from the code)

The Streamlit app (`Email Spam Classification streamlit.py`) does the following:

1. **Loads** two saved artifacts with `joblib`:
   - `spam_classifier_model.pkl` — the trained classifier
   - `tfidf_vectorizer.pkl` — the fitted TF-IDF vectorizer
2. **Preprocesses** the user's text the same way as during training:
   - Keeps only letters (`re.sub('[^a-zA-Z]', ' ', text)`)
   - Lower-cases and splits into words
   - Removes English **stopwords** (NLTK) and applies **Porter stemming**
3. **Vectorizes** the cleaned text with the TF-IDF vectorizer.
4. **Predicts** with the model:
   - `1` → 🚨 **Spam**
   - `0` → ✅ **Not Spam** (with balloons / snow animation)

```python
def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [ps.stem(word) for word in text if word not in stopwords.words('english')]
    return ' '.join(text)

cleaned = preprocess(user_input)
vectorized = vectorizer.transform([cleaned]).toarray()
prediction = model.predict(vectorized)[0]   # 1 = Spam, 0 = Ham
```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `Email Spam Classification streamlit.py` | Streamlit web app for live predictions |
| `Email Spam Classification.ipynb` | Notebook: EDA, preprocessing & model training |
| `spam.csv` | Labeled spam/ham dataset used for training |
| `spam_classifier_model.pkl` | Trained classifier (saved with joblib) |
| `tfidf_vectorizer.pkl` | Fitted TF-IDF vectorizer |
| `README.md` | This file |

---

## 🚀 Run It

```bash
# 1. Install dependencies
pip install streamlit scikit-learn nltk joblib

# 2. Run the app (from inside this folder)
streamlit run "Email Spam Classification streamlit.py"
```

Then open the local URL (usually http://localhost:8501), paste an email, and click **🔍 Check Spam**.

---

## 🛠️ Tech Stack

Python · scikit-learn · NLTK (stopwords + Porter stemmer) · TF-IDF · Streamlit · joblib
