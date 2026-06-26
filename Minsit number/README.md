# MNIST Digit Recognition Project

A machine learning project for recognizing handwritten digits (0-9) using the famous **MNIST dataset**. The project includes model training, evaluation, and a user-friendly web interface built with **Streamlit**.

## 📋 Project Overview

- **Dataset**: MNIST (Handwritten digits)
- **Models**: SVM and Logistic Regression (with saved pickle files)
- **Interface**: Streamlit web app for real-time digit prediction
- **Additional Files**: Jupyter notebook for experimentation and training

## ✨ Features

- Train and evaluate SVM and Logistic Regression models on MNIST
- Save and load pre-trained models (`svm_model.pkl`, `logistic_model.pkl`)
- Data preprocessing with scaler (`scaler.pkl`)
- Interactive Streamlit dashboard for drawing/predicting digits
- Sample digit images for testing
- Jupyter notebook for detailed analysis and model development

## 🛠️ Project Structure

```
Minsit number/
├── Mnist Digit Recognition Streamlit app.py    # Main Streamlit application
├── Mnist Digit Recognition.ipynb               # Jupyter notebook for training & analysis
├── svm_model.pkl                               # Trained SVM model
├── logistic_model.pkl                          # Trained Logistic Regression model
├── scaler.pkl                                  # Fitted StandardScaler
├── *.png                                       # Sample digit images (2.png, 4.png, etc.)
└── README.md
```

## 🚀 How to Run

### Prerequisites
```bash
pip install streamlit pandas numpy scikit-learn pillow matplotlib joblib
```

### Run the Streamlit App
```bash
streamlit run "Mnist Digit Recognition Streamlit app.py"
```

### Explore the Notebook
Open `Mnist Digit Recognition.ipynb` in Jupyter Notebook / JupyterLab / VS Code.

## 📊 Models Used

1. **Support Vector Machine (SVM)**
2. **Logistic Regression**

Both models are trained on the MNIST dataset with proper scaling.

## 🔧 Technologies Used

- **Python**
- **Scikit-learn** (Machine Learning)
- **Streamlit** (Web Interface)
- **Pandas & NumPy** (Data handling)
- **Pillow / Matplotlib** (Image processing)
- **Joblib** (Model serialization)

## 📸 Screenshots

*(Add screenshots of your Streamlit app here)*

## 🎯 Future Improvements

- Add CNN (Convolutional Neural Network) model for better accuracy
- Deploy on Streamlit Cloud / Hugging Face Spaces
- Add model comparison dashboard
- Improve UI with custom styling
- Add confidence scores and explanations

## 👤 Author

Your Name

---

**Made with ❤️ for learning Machine Learning**
