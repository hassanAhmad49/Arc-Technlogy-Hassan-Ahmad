# 🤖 Machine Learning Internship Projects — Arc Technologies

A collection of four end-to-end **Machine Learning** mini-projects built during my internship at **Arc Technologies**.
Each project covers the full workflow — data, model training in a Jupyter notebook, a saved model, and an interactive **Streamlit** web app for live predictions.

> **Author:** Hassan Ahmad

---

## 📂 Projects

| # | Project | Problem Type | Model | Folder |
|---|---------|--------------|-------|--------|
| 1 | 📧 **Email Spam Classification** | Text classification | TF-IDF + scikit-learn classifier | [`Email Spam`](./Email%20Spam) |
| 2 | 🏡 **House Price Prediction** | Regression | Random Forest Regressor | [`house price predection app`](./house%20price%20predection%20app) |
| 3 | 🌸 **Iris Flower Classification** | Multi-class classification | K-Nearest Neighbors (KNN) | [`Iris Flower Classification`](./Iris%20Flower%20Classification) |
| 4 | 🖊️ **MNIST Digit Recognition** | Image classification | Logistic Regression + SVM | [`Minsit number`](./Minsit%20number) |

Each folder has its own detailed `README.md` explaining the code.

---

## 🧩 What Each Project Does

- **Email Spam** — Cleans text (regex, NLTK stopwords, Porter stemming), converts it to TF-IDF features, and predicts **Spam vs. Not Spam**.
- **House Price** — Takes 8 California-housing inputs, engineers 3 extra features (11 total), and predicts the **house price**.
- **Iris** — Takes 4 sepal/petal measurements and predicts one of **3 Iris species** with a KNN model.
- **MNIST** — Takes an uploaded image, resizes to 28×28 grayscale, scales it, and predicts the **digit (0–9)** with two models.

---

## 🛠️ Common Tech Stack

- **Language:** Python
- **ML:** scikit-learn
- **Data:** Pandas, NumPy
- **Web UI:** Streamlit
- **Model I/O:** joblib / pickle
- **Extras:** NLTK (Email Spam), Pillow & OpenCV (MNIST)

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone <your-repo-url>
cd "Arc Technlogy Hassan Ahmad"

# Pick a project folder, install its dependencies, then run its app, e.g.:
cd "Iris Flower Classification"
pip install streamlit scikit-learn numpy joblib
streamlit run "Iris Flower Classification streamlit.py"
```

Each project's README lists the exact `pip install` line and `streamlit run` command.

---

## 📜 License

Released under the **MIT License** — free to use for learning.

---

**Made with ❤️ during the Arc Technologies ML Internship.**
