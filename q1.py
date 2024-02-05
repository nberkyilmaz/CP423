import nltk
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [re.sub('[^a-zA-Z]', ' ', token) for token in tokens]
    tokens = [token.strip() for token in tokens]
    tokens = [token for token in tokens if len(token) > 1]
    return tokens
