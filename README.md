Certainly! Here's the updated `README.md` content with a clear note about the **dataset download link** and your **GitHub repository link** added properly:

---

# 📩 SMS Spam Classifier (BoW)

A machine learning model that classifies SMS messages as spam or ham (non-spam) using Bag-of-Words (BoW) with enhanced preprocessing.

![Demo Screenshot](assets/image.png)

---

## 🔍 Overview

This project implements a robust SMS spam classifier using:

* **Bag-of-Words (BoW)** representation with `CountVectorizer`
* **Multinomial Naive Bayes** classification algorithm
* **Enhanced text preprocessing** with lemmatization and bigrams
* **Probability calibration** to reduce overconfident predictions

**Model Accuracy**: 98.2%
**Spam Recall**: 91%

---

## 📦 Dataset

The dataset used for training this model is the **SMS Spam Collection**.
📥 **Download it from here**: [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
Ensure it is placed in the `assets/data/` directory and named `SMSSpamCollection` (a tab-separated `.txt` file with no extension).

---

## 🛠️ Features

### Advanced Text Processing

* Lemmatization (more accurate than stemming)
* Bigram support to capture important phrases
* Comprehensive stopword removal
* Punctuation and number removal

### Optimized Classification

* Class weighting to handle imbalance
* Precision-recall optimized threshold
* Probability calibration for confidence scoring

### Easy-to-Use Interface

* Streamlit web app for interactive testing
* Clear confidence scores
* Visual feedback for user input

---

## 🚀 Quick Start

### Prerequisites

* Python 3.8+
* `pip` package manager

### Installation

Clone the repository:

```bash
git clone https://github.com/asmaa-2ahmed/spam-or-ham.git
cd spam-or-ham
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Web App

```bash
streamlit run main.py
```

The app will launch in your default browser at [http://localhost:8501](http://localhost:8501).

---

## 🧠 Model Training

To retrain the model with custom data:

1. Place your dataset in `assets/data/` and name it `SMSSpamCollection`
2. Run the training script:

```bash
python src/train.py
```

This will:

* Preprocess the data
* Train a new model
* Save updated model files to `assets/models/`
* Generate evaluation metrics

---

## 🧪 Testing the Model

Try these example messages:

**Spam Examples**:

* "Congratulations! You won a \$1000 gift card! Click here: bit.ly/freeprizes"
* "URGENT: Your account has been locked. Verify now: secure-login.com"

**Ham Examples**:

* "Hey, running late for dinner. Will be there by 8"
* "Your Amazon verification code is 794321. Expires in 15 minutes."

---

## 🛠️ Technical Details

### Data Preprocessing Pipeline

* Lowercasing
* Punctuation removal
* Tokenization
* Lemmatization (using `WordNetLemmatizer`)
* Stopword removal
* Bigram generation

### Model Architecture

* **Vectorizer**: `CountVectorizer` with 5,000 features
* **Classifier**: Multinomial Naive Bayes with class weighting
* **Threshold**: Optimized via precision-recall analysis

### Performance Metrics

| Metric         | Score |
| -------------- | ----- |
| Accuracy       | 98.2% |
| Spam Recall    | 91%   |
| Spam Precision | 89%   |
| ROC AUC        | 0.992 |

---

## 🤝 Contributing

We welcome contributions!
To contribute:

1. Fork the repository
2. Create a feature branch:
   `git checkout -b feature/your-feature`
3. Commit your changes:
   `git commit -m 'Add some feature'`
4. Push to the branch:
   `git push origin feature/your-feature`
5. Open a Pull Request

---

## 🔗 Repository

View the full source code here:
👉 [https://github.com/asmaa-2ahmed/spam-or-ham](https://github.com/asmaa-2ahmed/spam-or-ham)

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

Let me know if you’d like to also generate a Markdown file or add badges for Python version, license, etc.
