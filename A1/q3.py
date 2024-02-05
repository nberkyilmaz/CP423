#Import inverted index
from q2 import build_inverted_index

def evaluate_query(inverted_index, query):
    # Tokenize the query based on spaces, assuming a space-delimited format
    tokens = query.upper().split()
    # Initialize an empty result set
    result_set = None
    # Keep track of the current operator
    current_operator = None

    for token in tokens:
        if token in ['AND', 'OR', 'NOT']:
            # Update the current operator if an operator token is encountered
            current_operator = token
        else:
            # Convert the token to lowercase for consistent matching
            token = token.lower()
            # Retrieve the document set for the current token (word) from the inverted index
            current_set = inverted_index.get(token, set())

            if current_operator == 'AND':
                # Intersect with the result set if the operator is AND
                result_set = result_set & current_set if result_set is not None else current_set
            elif current_operator == 'OR':
                # Union with the result set if the operator is OR
                result_set = result_set | current_set if result_set is not None else current_set
            elif current_operator == 'NOT':
                # Subtract from the result set if the operator is NOT
                if result_set is not None:
                    result_set = result_set - current_set
                else:
                    # If there's no result set yet, initialize it to all documents minus the NOT set
                    all_documents = set.union(*inverted_index.values())
                    result_set = all_documents - current_set
            else:
                # Initialize result_set with the current set if no operator is set 
                result_set = current_set

            # Reset the operator after processing
            current_operator = None

    return result_set

if __name__ == "__main__":
    # Build the inverted index from the files in data set 
    inverted_index = build_inverted_index()

    # Define queries to test the inverted index
    queries = [
        "Holmes OR Watson",
        "Holmes AND Watson",
        "Holmes AND NOT Moriarty",
        "Holmes OR NOT Lestrade"
    ]

    # Test executing the complex queries against the inverted index
    for query in queries:
        result_files = evaluate_query(inverted_index, query)
        print(f"Query '{query}' found in files: {result_files}")