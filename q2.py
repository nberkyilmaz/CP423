# Required imports
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



# Download necessary NLTK data

nltk.download('punkt')
nltk.download('stopwords')


# Define the path to the directory containing your text files
path = "/Users/ayushchhetri/Desktop/cp423/CP423/Assignment1/data"
os.chdir(path)

# Function to preprocess text in each file
def preprocess_text(file_path):
    with open(file_path, 'r', encoding='iso-8859-1') as f:
        text = f.read()
    
    text = text.lower()  # Convert text to lowercase
    tokens = word_tokenize(text)  # Tokenize the text

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word.isalpha()]

    # Eliminate singly occurring characters
    tokens = [word for word in tokens if len(word) > 1]

    return tokens

# Function to build the inverted index
def build_inverted_index():
    inverted_index = {}

    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            words = preprocess_text(file_path)

            for word in words:
                if word not in inverted_index:
                    inverted_index[word] = set()
                inverted_index[word].add(file)

    return inverted_index

# Function to query the inverted index
def query_inverted_index(word, inverted_index):
    word = word.lower()  # Ensure the word is in lowercase to match preprocessing
    return inverted_index.get(word, set())

# Main code to build the inverted index and test it
if __name__ == "__main__":
    # Build the inverted index from the files in the specified directory
    inverted_index = build_inverted_index()

    # Define a set of test words to query in the inverted index
    test_words = ["Holmes", "Fleric", "Lestrade"]  

    # Test querying the inverted index with the specified words
    for word in test_words:
        files = query_inverted_index(word, inverted_index)
        print(f"Word '{word}' found in files: {files}")
