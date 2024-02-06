# Import necessary modules and functions from previous questions
from q1 import preprocess_text
from q2 import build_inverted_index
from q3 import evaluate_query
import os

# Initialize global variables to store document names and the inverted index
documents = {}
invertedIndex = {}

if __name__ == "__main__":
    invertedIndex, documents = build_inverted_index()  # Create the inverted index from documents
    query_number = int(input("How many queries are you running? "))
    for i in range(query_number):
        print(f"\nQuery #{i+1}:")
        user_input_sentence = input("Input Sentence: ")
        user_input_operation_sequence = input("Input operation sequence: ")
        operators = user_input_operation_sequence.strip().split(",")
        # Preprocess the user input sentence
        preprocessed_sentence = preprocess_text(user_input_sentence)
        preprocessed_query = ""
        operator_index = 0
        # Construct the preprocessed query with operators
        for word in preprocessed_sentence:
            preprocessed_query += f"{word} "
            if operator_index < len(operators):
                preprocessed_query += f"{operators[operator_index]} "
            operator_index += 1
        preprocessed_query = preprocessed_query.strip()
        print(f"Expected preprocessed query: \"{preprocessed_query}\"")
        # Evaluate the query and obtain results
        result, total_comparisons = evaluate_query(invertedIndex, preprocessed_query)
        # Print the query evaluation results
        print("Output:")
        print("Number of matched documents:", len(result))
        print("Minimum number of comparisons required:", total_comparisons)
        # Print details of the retrieved documents
        for documentId in sorted(result):
            print(f"{documents[documentId]} | ID= {documentId}")
