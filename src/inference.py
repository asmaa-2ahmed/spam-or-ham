from joblib import load
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


from .config import MODEL_PATH, VECTORIZER_PATH

# Load model
model = load(MODEL_PATH)
vectorizer = load(VECTORIZER_PATH)

sample = ["Congrats! You've won a free ticket"]
vectorized = vectorizer.transform(sample)
prediction = model.predict(vectorized)

print("Prediction:", prediction)


# --- Preprocessing Function ---

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    text = ' '.join(words)
    text = re.sub(r'\s+', ' ', text).strip()

    return text



# --- Inference Function ---
def predict_message(text):
    cleaned = preprocess_text(text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    proba = model.predict_proba(vectorized).max()
    return prediction, proba
