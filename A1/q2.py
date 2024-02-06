# Required imports
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from q1 import preprocess_text

#Global Variables
documents = {}
invertedIndex = {}

# Download necessary NLTK data

nltk.download('punkt')
nltk.download('stopwords')


# Define the path to the directory containing your text files
path = "/Users/ayushchhetri/Desktop/cp423/CP423/Assignment1/data"
os.chdir(path)


# Function to build the inverted index
def build_inverted_index():
    global documents, invertedIndex
    path = "/Users/ayushchhetri/Desktop/cp423/CP423/Assignment1/data"
    os.chdir(path)
    documentId = 1
    for file in os.listdir():
        if file.endswith(".txt"):
            filePath = f"{path}/{file}"
            words = preprocess_text(open(filePath, "r", encoding="iso-8859-1").read())
            for word in words:
                if word not in invertedIndex:
                    invertedIndex[word] = set()
                invertedIndex[word].add(documentId)
            documents[documentId] = file
            documentId += 1
    return invertedIndex, documents



