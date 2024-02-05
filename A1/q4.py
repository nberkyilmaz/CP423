from q1 import preprocess_text  
from q2 import build_inverted_index  
from q3 import evaluate_query  
import os

documents = {}
invertedIndex = {}

def createInvertedIndex():
    global documents, invertedIndex
    path = "/Users/ayushchhetri/Desktop/cp423/CP423/Assignment1/data" 
    os.chdir(path)
    documentId = 1
    for file in os.listdir():
        if file.endswith(".txt"):  
            filePath = file
            words = preprocess_text(open(filePath, "r", encoding="utf-8").read())
            for word in words:
                if word not in invertedIndex:
                    invertedIndex[word] = set()
                invertedIndex[word].add(documentId)
            documents[documentId] = file
            documentId += 1

if __name__ == "__main__":
    createInvertedIndex()  
    query_number = int(input("How many queries are you running? "))
    for i in range(query_number):
        print(f"Query #{i+1}:")
        user_input_sentence = input("Input Sentence: ")
        user_input_operation_sequence = input("Input operation sequence: ")
        operators = user_input_operation_sequence.strip().split(",")
        preprocessed_sentence = preprocess_text(user_input_sentence)
        preprocessed_query = ""
        operator_index = 0
        for word in preprocessed_sentence:
            if operator_index < len(operators):
                preprocessed_query += f"{word} {operators[operator_index]} "
            else:
                preprocessed_query += word
            operator_index += 1
        preprocessed_query = preprocessed_query.strip()
        print("\nExpected preprocessed query:", preprocessed_query)
        result = evaluate_query(invertedIndex, preprocessed_query)
        print("\nOutput:")
        print("Number of matched documents:", len(result))
        for documentId in result:
            print(f"{documents[documentId]} | ID= {documentId}")
