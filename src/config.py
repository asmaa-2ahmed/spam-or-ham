import os

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
DATA_PATH = os.path.join(ASSETS_DIR, 'data', 'SMSSpamCollection')
MODEL_PATH = os.path.join(ASSETS_DIR, 'models', 'spam_model.pkl')
VECTORIZER_PATH = os.path.join(ASSETS_DIR, 'models', 'bow_vectorizer.pkl')
