# 🖊️ MNIST Digit Recognition

A machine learning web app that recognizes a handwritten digit (0–9) from an uploaded image.
It uses two scikit-learn models — **Logistic Regression** and **SVM** — trained on the **MNIST** dataset,
with a shared **StandardScaler**, all served through a **Streamlit** app.

> Internship Task — Arc Technologies · Built by **Hassan Ahmad**

---

## 🧠 How It Works (from the code)

The app (`Mnist Digit Recognition Streamlit app.py`):

1. **Loads** three saved artifacts with `joblib`:
   - `logistic_model.pkl` — Logistic Regression model
   - `svm_model.pkl` — SVM model
   - `scaler.pkl` — fitted StandardScaler
2. **Accepts an uploaded image** (`png`, `jpg`, `jpeg`) and preprocesses it to match MNIST:
   ```python
   image = Image.open(uploaded_file).convert("L")   # grayscale
   img_resized = image.resize((28, 28))             # 28x28
   img_flat = np.array(img_resized).flatten().reshape(1, -1)  # 784 features
   img_scaled = scaler.transform(img_flat)          # scale like training
   ```
3. **Predicts** the digit with both models and shows the results:
   ```python
   log_pred = log_reg.predict(img_scaled)[0]
   svm_pred = svm_model.predict(img_scaled)[0]
   ```

> ℹ️ Tip: a 28×28 **black background with a white digit** matches the MNIST training format best.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `Mnist Digit Recognition Streamlit app.py` | Streamlit web app for digit prediction |
| `Mnist Digit Recognition.ipynb` | Notebook: training & analysis |
| `logistic_model.pkl` | Trained Logistic Regression model |
| `svm_model.pkl` | Trained SVM model |
| `scaler.pkl` | Fitted StandardScaler |
| `2.png`, `4.png`, `5.png`, `7.png`, `9.png`, `11.png` | Sample digit images for testing |
| `README.md` | This file |

---

## 🚀 Run It

```bash
# 1. Install dependencies
pip install streamlit scikit-learn numpy pillow opencv-python joblib

# 2. Run the app (from inside this folder)
streamlit run "Mnist Digit Recognition Streamlit app.py"
```

Upload one of the sample `.png` images (or your own handwritten digit) to get a prediction.

---

## 🛠️ Tech Stack

Python · scikit-learn (Logistic Regression + SVM) · NumPy · Pillow · OpenCV · Streamlit · joblib
**Dataset:** MNIST handwritten digits (28×28 grayscale)
