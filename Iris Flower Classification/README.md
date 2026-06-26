# 🌸 Iris Flower Classification

A machine learning web app that classifies an Iris flower into one of three species —
**Setosa**, **Versicolor**, or **Virginica** — using a pre-trained **K-Nearest Neighbors (KNN)** model.
The interface is built with **Streamlit**.

> Internship Task — Arc Technologies · Built by **Hassan Ahmad**

---

## 🧠 How It Works (from the code)

The app (`Iris Flower Classification streamlit.py`):

1. **Loads** the pre-trained KNN model from `iris_knn_model.joblib`
   (it checks the file exists and handles load errors gracefully).
2. **Takes 4 measurements** from the user via number inputs:
   - Sepal Length (cm)
   - Sepal Width (cm)
   - Petal Length (cm)
   - Petal Width (cm)
3. **Predicts** the species. The model returns a class index that maps to a name:
   ```python
   species_names = ['setosa', 'versicolor', 'virginica']
   input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
   prediction_index = model.predict(input_data)[0]
   predicted_species = species_names[prediction_index]
   ```
4. **Displays** the predicted species with a short description and celebratory balloons.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `Iris Flower Classification streamlit.py` | Streamlit web app for live predictions |
| `Iris Flower Classification.ipynb` | Notebook: EDA, model training & evaluation |
| `iris_knn_model.joblib` | Pre-trained KNN model (format used by the app) |
| `iris_knn_model.pkl` | Same model saved as a pickle file |
| `README.md` | This file |

---

## 🚀 Run It

```bash
# 1. Install dependencies
pip install streamlit scikit-learn numpy joblib

# 2. Run the app (from inside this folder)
streamlit run "Iris Flower Classification streamlit.py"
```

Enter the four flower measurements and click **Predict Species**.

---

## 🛠️ Tech Stack

Python · scikit-learn (KNN) · NumPy · Streamlit · joblib
**Dataset:** Classic Iris dataset (150 samples, 4 features, 3 species)
