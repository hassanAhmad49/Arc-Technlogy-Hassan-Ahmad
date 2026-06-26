# Email Spam Classification

A machine learning project for classifying emails as **Spam** or **Ham** (non-spam). Includes a Jupyter Notebook for model development and a Streamlit web application for interactive predictions.

## Features

- **Data Preprocessing**: Text cleaning, vectorization (TF-IDF), etc.
- **Machine Learning Models**: Trained classifiers (e.g., Naive Bayes, Logistic Regression, SVM, Random Forest, etc.)
- **Interactive Web App**: Built with Streamlit for easy email classification
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
- **Jupyter Notebook**: Full exploratory data analysis and model training

## Project Structure

```
Email-Spam-Classification/
├── Email Spam Classification.ipynb     # Jupyter Notebook (EDA + Modeling)
├── Email Spam Classification streamlit.py  # Streamlit Web Application
├── requirements.txt                    # Python dependencies
├── data/                               # Dataset folder (if included)
├── models/                             # Saved trained models
└── README.md
```

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Email-Spam-Classification.git
   cd Email-Spam-Classification
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**
   ```bash
   streamlit run "Email Spam Classification streamlit.py"
   ```

4. **Open Jupyter Notebook** (optional)
   ```bash
   jupyter notebook "Email Spam Classification.ipynb"
   ```

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- NLTK / Text processing
- Streamlit (for web UI)
- Matplotlib / Seaborn (visualizations)

## How to Use the App

1. Run the Streamlit command above
2. Open the local URL (usually http://localhost:8501)
3. Paste an email text into the input box
4. Click **Classify** to get Spam / Ham prediction with confidence score

## Dataset

The model was trained on a publicly available spam/ham email dataset.

## Future Improvements

- Add deep learning models (LSTM, BERT)
- Email integration (fetch from Gmail/IMAP)
- Bulk classification
- Model deployment (Hugging Face / Heroku / AWS)

## Contributing

Pull requests are welcome! Feel free to open issues for bugs or feature requests.

## License

MIT License

---

**Made with ❤️ for learning and spam prevention**
