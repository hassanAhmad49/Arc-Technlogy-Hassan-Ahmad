# 🌸 Iris Flower Classification Project

A classic machine learning project to classify Iris flowers into three species (**Setosa**, **Versicolor**, and **Virginica**) using sepal and petal measurements.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Models Used](#models-used)
- [Results](#results)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
This project demonstrates the complete machine learning workflow:
- Exploratory Data Analysis (EDA)
- Data visualization
- Model training & evaluation
- Model deployment (Streamlit web app)

It is an excellent beginner-to-intermediate project for understanding classification algorithms.

---

## Dataset
The project uses the famous **Iris Dataset** by Ronald Fisher.

- **Total samples**: 150
- **Features**: 4 (Sepal Length, Sepal Width, Petal Length, Petal Width)
- **Target**: 3 species (Setosa, Versicolor, Virginica)
- **Source**: UCI Machine Learning Repository / scikit-learn

---

## Features
- Comprehensive EDA with visualizations
- Multiple classification models
- Model performance comparison
- Interactive web application using **Streamlit**
- Model saving & loading
- Easy prediction interface

---

## Project Structure
```
Iris Flower Classification/
├── Iris Flower Classification streamlit.py    # Main Streamlit App
├── requirements.txt                           # Dependencies
├── model/                                     # Saved models (if any)
├── notebooks/                                 # Jupyter notebooks (EDA)
├── data/                                      # iris.csv (if included)
├── README.md
└── screenshots/                               # (optional)
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Iris-Flower-Classification
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Run Streamlit App
```bash
streamlit run "Iris Flower Classification streamlit.py"
```

### Or run Jupyter Notebook (if available)
```bash
jupyter notebook
```

---

## Models Used
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Decision Tree

**Best Model**: Usually SVM or Random Forest (depends on your training)

---

## Results
(Replace this section with your actual results)

| Model                | Accuracy | Precision | Recall | F1-Score |
|----------------------|----------|-----------|--------|----------|
| Logistic Regression  | 0.97     | 0.97      | 0.97   | 0.97     |
| SVM                  | **0.98** | 0.98      | 0.98   | 0.98     |
| Random Forest        | 0.96     | 0.96      | 0.96   | 0.96     |

---

## Technologies
- **Python**
- **scikit-learn**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **Streamlit** (for web app)
- **Joblib** (model saving)

---

## Contributing
Feel free to fork this project and submit pull requests. Any improvements are welcome!

---

## License
This project is open-source and available under the **MIT License**.

---

**Made with ❤️ for learning Machine Learning**