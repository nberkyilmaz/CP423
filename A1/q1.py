# Import necessary libraries for text processing
import nltk
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK datasets for tokenization and stopword removal
nltk.download('punkt')  # Dataset for tokenization
nltk.download('stopwords')  # Dataset for stopwords

def preprocess_text(text):
    """
    Preprocess the input text by lowercasing, tokenizing, removing stopwords,
    excluding non-alphabetic characters, and eliminating single character words.
    
    Parameters:
    - text (str): The text to preprocess.
    
    Returns:
    - list: A list of preprocessed tokens from the input text.
    """
    text = text.lower()  # Convert text to lowercase to normalize case sensitivity
    tokens = word_tokenize(text)  # Tokenize the text into individual words
    stop_words = set(stopwords.words('english'))  # Retrieve the set of English stopwords
    tokens = [token for token in tokens if token not in stop_words]  # Remove stopwords from tokens
    tokens = [re.sub('[^a-zA-Z]', ' ', token) for token in tokens]  # Remove non-alphabetic characters
    tokens = [token.strip() for token in tokens]  # Strip whitespace from tokens
    tokens = [token for token in tokens if len(token) > 1]  # Remove single character words
    return tokens  # Return the list of processed tokens