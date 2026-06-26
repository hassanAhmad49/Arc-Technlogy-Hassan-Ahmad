# 🏡 House Price Prediction App

A machine learning web app that predicts a house price from the **California Housing** features.
A regression model (Random Forest) is trained in the notebook, saved to a pickle file, and served through an interactive **Streamlit** app.

> Internship Task 3 — Arc Technologies · Built by **Hassan Ahmad**

---

## 🧠 How It Works (from the code)

The app (`House price predication app.py`):

1. **Loads** the model from `housing_model12.pkl`. The pickle stores a **dictionary**, and the model is taken from the `'model'` key:
   ```python
   with open("housing_model12.pkl", "rb") as file:
       model_dict = pickle.load(file)
       model = model_dict['model']
   ```
2. **Takes 8 base inputs** from the user:
   Median Income, House Age, Average Rooms, Average Bedrooms, Population, Average Occupancy, Latitude, Longitude.
3. **Engineers 3 extra features** at prediction time, giving **11 features** total:
   ```python
   rooms_per_person        = avg_rooms / avg_occupancy
   bedrooms_per_room       = avg_bedrooms / avg_rooms
   population_per_household = population / avg_occupancy
   ```
   (each guarded against division by zero)
4. **Predicts** and displays the price (the raw prediction is scaled by ×100 for display):
   ```python
   prediction = model.predict(input_data)
   st.success(f"congratulations House Price: ${prediction[0]*100:.2f}")
   ```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `House price predication app.py` | Streamlit web app for price prediction |
| `house pridect model.ipynb` | Notebook: data cleaning, feature engineering, training |
| `housing_model12.pkl` | Saved model (stored inside a dict under key `model`) |
| `house 1.mp4` | Demo recording of the running app |
| `house price.txt` | Project summary / write-up |
| `README.md` | This file |

---

## 🚀 Run It

```bash
# 1. Install dependencies
pip install streamlit scikit-learn numpy

# 2. Run the app (from inside this folder)
streamlit run "House price predication app.py"
```

Enter the property details and click **Predict** to get an estimated price.

---

## 🛠️ Tech Stack

Python · scikit-learn (Random Forest Regression) · NumPy · Streamlit · pickle
**Dataset:** California Housing dataset
